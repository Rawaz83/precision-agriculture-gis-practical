# Precision Agriculture & GIS — Practical

**University of Sulaimani — College of Agricultural Engineering Sciences**  
**Lecturer:** Rawaz Hama Ali  
**Academic year:** 2026–2027  
**Instruction language:** English

Open educational resource with 14 applied agricultural GIS lectures, original third-party teaching photographs/diagrams and YouTube tutorials, downloadable synthetic datasets, and browser-based formative exercises.

## Course access

- [14-lecture course](https://rawaz83.github.io/precision-agriculture-gis-practical/)
- [Lecture 1 interactive farm laboratory](https://rawaz83.github.io/precision-agriculture-gis-practical/files/interactive-lab.html)
- [Lecture 6 interactive QGIS laboratory](https://rawaz83.github.io/precision-agriculture-gis-practical/files/qgis-training-lab.html)
- [11-module interactive hub — Lectures 3–5 and 7–14](https://rawaz83.github.io/precision-agriculture-gis-practical/files/course-interactives.html)
- [Practice data and provenance](data/)

## Publishing architecture

The Carpentries Workbench builds Markdown files from the `main` branch into the generated `gh-pages` branch. Standalone HTML files are stored in `files/` and synced by the workflow `.github/workflows/publish-interactive-lab.yaml` after successful course builds. The original lesson files and external credited media remain in their existing structure.

## Privacy, assessment and data integrity

Practice progress and quiz results are saved only in the student's own browser when local storage is permitted. There is no authenticated student identity or gradebook. Results can be self-reported or reset and **must not be treated as formal grades**. Students submit actual GIS files through university-approved means.

**All internally created practice data are synthetic**, not actual farm boundaries, measured soil chemistry, real drone surveys or field prescriptions. Original course text and synthetic training data are CC BY 4.0 unless stated otherwise. External images, source datasets and videos retain their respective owners' license terms. See individual lesson captions and [CITATION.cff](CITATION.cff).

## Moodle and modeled regional GIS resources

- [Moodle XML formative question bank (65 questions)](moodle/GIS_Moodle_Question_Bank.xml); [14 assignment/rubric briefs](moodle/ASSIGNMENTS_AND_RUBRICS.md).
- [Moodle setup instructions](moodle/README.md). The connected GitHub integration cannot reach the lecturer's local Moodle installation, so actual quizzes/assignments **have not been created in Moodle**.
- [Interactive regional data explorer](https://rawaz83.github.io/precision-agriculture-gis-practical/files/regional-data-lab.html).
- [NASA POWER-derived regional data and scientific caveats](data/regional/README.md). These are derived earlier summary files, not authenticated direct NASA API responses or weather/soil station observations.
