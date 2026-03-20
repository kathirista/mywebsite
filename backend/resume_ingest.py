import os
import chromadb
from sruthiAI import NewGoogleEmbeddingFunction, API_KEY, DB_PATH

# 1. Connect to the EXISTING database
chroma_client = chromadb.PersistentClient(path=DB_PATH)
embedding_fn = NewGoogleEmbeddingFunction(api_key=API_KEY)
collection = chroma_client.get_collection(name="blogs", embedding_function=embedding_fn)
#print(DB_PATH)
# 2. Prepare your Resume Data
resume_sections = [
    "1. Professional Profile & Core IdentitySummary: A Data Science and AI professional with over 8 years of experience at major automotive companies like BMW, Audi, and VW. Specializes in connecting raw data to production-ready insights, such as sensor logs and perception training pipelines.Key Strengths: Expert in architecting scalable AWS ecosystems (Athena, Lambda, Glue) for high-dimensional data mining and early adopter of LLM-augmented engineering.2. Specialized Technical Skill SetsAI & Machine Learning: Deep experience in GAN-based synthetic data generation, network pruning, and computer vision research. Proficient with tools like Claude code, Gemini CLI, and Google AI Studio.Data Engineering & Automation: Advanced skills in Python, SQL, and UI Path for process automation. Expert in building real-time monitoring dashboards using AWS QuickSight and PowerBI.3. Key Career Milestones (Work Experience)BMW Motorcycles (Berlin): Served as Digitization and Process Automation Lead. Automated data mining pipelines for autonomous vehicle sensor logs and reduced assembly line downtime by 80% using predictive machine learning models.Audi AG (Germany): Led the pivot from Excel-based reporting to Python and SQL solutions for 31 European markets. Managed massive-scale IT compliance and audit recovery.Volkswagen AG (Wolfsburg/California): Conducted research at the Electronics Research Lab in California, optimizing object detection for autonomous vehicles through network pruning.4. Education & Academic ResearchM.Sc. in Information and Automation Engineering: University of Bremen, Germany, focusing on AI, Machine Learning, and Robotics.Master's Thesis: Developed a computer vision pipeline using GANs and datasets like KITTI and Cityscapes to synthesize realistic traffic environments for training perception models.5. Personal Projects (AI Twin Context)Sruthi AI Twin: Built a custom digital twin using a RAG pipeline and six years of personal blog posts stored in a vector database.AI Tooling: Developed a job-finder app on Google AI Studio and a React component generator using Claude code.",
    "Skills: Python, SQL, Google Cloud, Docker, ChromaDB, and Biking through the Alps."
]

# 3. Add them (Use a unique prefix for IDs so they don't clash with blog IDs)
collection.add(
    documents=resume_sections,
    ids=[f"resume_chunk_{i}" for i in range(len(resume_sections))]
)

#print(f"Successfully added {len(resume_sections)} resume parts to the database!")