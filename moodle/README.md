# Moodle import-ready assessment materials

These files are designed to be imported into **Moodle 5.x**; they have
**not yet been imported into a live Moodle server**. The previously
discussed `moodle.test` site runs locally on the lecturer's computer,
which this ChatGPT GitHub integration cannot remotely administer.

## Question bank

- `GIS_Moodle_Question_Bank.xml` contains **65 questions**:
  44 multiple-choice questions adapted from the course-wide
  interactive modules, plus questions for Lectures 1, 2, 6, and NASA POWER
  data provenance. Every item has one correct answer, distractors, explanatory
  feedback, and a 1-mark default grade. Questions are separated by
  `$course$/top/Precision Agriculture GIS/Week XX` category hints.
- To import: open your own Moodle course, go to **Question bank → Import**,
  select **Moodle XML format**, choose the XML file, preview and confirm
  the incoming questions. Depending on Moodle version, category behavior
  may differ. Review a small import first, and check question categories.
- Create one formative practice quiz per lecture and manually select the
  relevant questions from its imported category. Set attempts, grade-to-pass,
  time and review options in Moodle according to your academic policy.
- Use **Moodle Assignment activities** for student file submissions, not
  the browser-saved progress scores.

## Rubrics and graded student assignments

- See `ASSIGNMENTS_AND_RUBRICS.md` for 14 practical submission descriptions
  and 10-point marking criteria. Assignments are **authoring specifications**
  until you create real Assignment activities in Moodle.
- Enable Assignment → Grade → Grading method → Rubric.
  Create levels for each criterion, publish rubric to students, and test
  with a non-student preview.
- Keep sensitive student files and grades inside institutional Moodle.
  The GitHub website is open and has no secure student authentication.

## Quality warnings

- Question accuracy should be reviewed by the subject lecturer before
  the bank is used for high-stakes assessment.
- Graded quiz question banks should not be published publicly if answer
  secrecy is needed. This public bank is **formative/sample material**;
  create a private variant in Moodle for summative exams.
- Datasets in the original course are synthetic; the new NASA POWER
  tables are regional reanalysis-derived summaries whose original API
  responses were not independently retained. Neither supports field
  agronomic prescriptions.

Official documentation:
https://docs.moodle.org/501/en/Importing_questions
https://docs.moodle.org/503/en/Rubric
https://docs.moodle.org/25/en/Moodle_XML_format
