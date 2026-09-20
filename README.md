HireFit Analyzer helps students and job seekers understand how well their profile matches a target role and prepares them for the interview that follows. The user uploads a resume and a job description. The system chunks both documents, converts them into embeddings, and stores them in a vector database. It then retrieves the most relevant sections and passes them to a large language model, which produces a structured placement report and a tailored question set.

Key features

Resume-to-JD match score with a breakdown by skills, experience, and education
Matching and missing skill detection
Skill gap analysis with suggestions on what to learn or add
Resume improvement tips, such as rewording bullet points and highlighting relevant projects
ATS-friendliness check
Interview question generation:
Technical questions based on the skills required in the JD
Resume-based questions on the candidate's own projects, internships, and experience
Behavioral and HR questions tailored to the role
Gap-focused questions on weak areas the interviewer is likely to probe
Difficulty levels (easy, medium, hard), with optional sample answers or answer hints
Context-grounded output via RAG, which reduces hallucination

How it works

Upload the resume (PDF/DOCX) and paste or upload the JD.
Parse and chunk the text, then generate embeddings.
Store the embeddings in a vector database (FAISS or ChromaDB).
Retrieve the relevant chunks for each JD requirement and resume section.
The LLM generates the match score, gap analysis, and improvement tips.
The LLM then generates interview questions from the retrieved context, covering both what the JD demands and what the resume claims.
Everything is shown in a single report in the UI.
