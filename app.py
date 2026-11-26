
import os

from flask import Flask, flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

from config import ALLOWED_EXTENSIONS, MAX_CONTENT_LENGTH, UPLOAD_FOLDER
from utils.matching_engine import MatchingEngine
from utils.resume_parser import parse_resume
from utils.skill_extractor import SkillExtractor


app = Flask(__name__, static_folder="statics")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-only-change-in-production")

os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/favicon.ico", methods=["GET"])
def favicon():
    return "", 204


@app.route("/analyze", methods=["POST"])
def analyze():
    resume = request.files.get("resume")
    job_description = request.form.get("job_description", "").strip()

    if resume is None or resume.filename == "":
        flash("Please choose a resume file.", "error")
        return redirect(url_for("home"))

    if not allowed_file(resume.filename):
        flash("Only PDF and DOCX resume files are supported.", "error")
        return redirect(url_for("home"))

    if len(job_description) < 20:
        flash("Please enter a job description with at least 20 characters.", "error")
        return redirect(url_for("home"))

    filename = secure_filename(resume.filename)
    saved_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    try:
        resume.save(saved_path)
        resume_text = parse_resume(saved_path)

        if not resume_text.strip():
            flash("No readable text was found in the resume.", "error")
            return redirect(url_for("home"))

        similarity = MatchingEngine().calculate_similarity(
            resume_text, job_description
        )
        skill_extractor = SkillExtractor()
        resume_skills = skill_extractor.extract_skills(resume_text)
        job_skills = skill_extractor.extract_skills(job_description)

        resume_skill_names = {
            skill
            for skills in resume_skills.values()
            for skill in skills
        }
        job_skill_names = {
            skill
            for skills in job_skills.values()
            for skill in skills
        }

        matched_skills = sorted(resume_skill_names & job_skill_names)
        missing_skills = sorted(job_skill_names - resume_skill_names)

        score = round(max(0.0, min(1.0, float(similarity))) * 100, 1)

        if score >= 75:
            verdict = "Strong match"
            verdict_class = "success"
        elif score >= 50:
            verdict = "Potential match"
            verdict_class = "warning"
        else:
            verdict = "Low match"
            verdict_class = "danger"

        return render_template(
            "result.html",
            score=score,
            verdict=verdict,
            verdict_class=verdict_class,
            resume_skills=resume_skills,
            matched_skills=matched_skills,
            missing_skills=missing_skills,
            filename=filename,
        )
    except (OSError, ValueError, TypeError) as exc:
        app.logger.exception("Unable to analyze resume")
        flash("The resume could not be analyzed: {}".format(exc), "error")
        return redirect(url_for("home"))
    finally:
        if os.path.exists(saved_path):
            os.remove(saved_path)


@app.errorhandler(413)
def file_too_large(_error):
    flash("The resume is too large. The maximum file size is 10 MB.", "error")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True,port=5000,host="0.0.0.0")

