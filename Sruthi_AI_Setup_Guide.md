# Guide to Making Sruthi AI Functional

This guide provides step-by-step instructions to connect your frontend (`knowledgeDB/index.html`) to the backend AI brain (`backend/sruthiAI.py` and `backend/main.py`), utilizing the `ChromaDB_Blogs` knowledge base.

## Step 1: Set Up and Run the Backend

Your backend is powered by FastAPI and uses `sruthiAI.py` to query the `ChromaDB_Blogs` database and generate answers using the Gemini API.

1. **Install Prerequisites**:
   Ensure you have Python installed. Open a terminal, navigate to your project's `backend` directory, and install the required packages (if you haven't already):
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
   *(Note: Ensure `fastapi`, `uvicorn`, `chromadb`, `google-genai`, and `python-dotenv` are in your `requirements.txt`.)*

2. **Verify API Key**:
   Ensure your `backend/.env` file contains your valid Gemini API key. It should look like this:
   ```env
   export GEMINI_API_KEY="your_api_key_here"
   ```

3. **Start the API Server**:
   From inside the `backend` directory, run the FastAPI server using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```
   The server will start running at `http://localhost:8000`. It exposes an endpoint at `POST /ask` which takes a JSON payload like `{"query": "your question"}`.

## Step 2: Update the Frontend (HTML/JS)

Your `knowledgeDB/index.html` currently has a search bar but no logic to send the question to the backend and display the answer. 

1. Open `knowledgeDB/index.html`.
2. Find the input field for the search bar and add an `id` to it (like `id="ai-search-input"`) so we can easily select it with JavaScript:
   ```html
   <input type="text" id="ai-search-input" class="search-bar" placeholder="What would Sruthi say?" aria-label="Ask Sruthi AI">
   ```
3. Add a designated area in the HTML to display the response and loading state. You can add this right below the search bar container (inside the `.glass-card`):
   ```html
   <div id="ai-response-container" class="mt-8 text-left hidden border border-gray-200 rounded-xl p-6 bg-white shadow-sm">
       <h3 class="font-bold text-rust mb-2">Sruthi AI says:</h3>
       <p id="ai-response-text" class="text-gray-700"></p>
   </div>
   ```
4. Add the following JavaScript just before the closing `</body>` tag to handle the request:
   ```html
   <script>
       const searchInput = document.getElementById('ai-search-input');
       const responseContainer = document.getElementById('ai-response-container');
       const responseText = document.getElementById('ai-response-text');

       searchInput.addEventListener('keypress', async function (e) {
           if (e.key === 'Enter') {
               const query = searchInput.value.trim();
               if (!query) return;

               // Show loading state
               responseContainer.classList.remove('hidden');
               responseText.innerHTML = '<i>Thinking...</i>';

               try {
                   // Make the API request to the FastAPI backend
                   const response = await fetch('http://localhost:8000/ask', {
                       method: 'POST',
                       headers: {
                           'Content-Type': 'application/json',
                       },
                       body: JSON.stringify({ query: query })
                   });

                   if (!response.ok) {
                       throw new Error('Network response was not ok');
                   }

                   const data = await response.json();
                   
                   // Display the AI's response
                   // Replace newline characters with <br> tags for correct HTML formatting
                   responseText.innerHTML = data.answer.replace(/\n/g, '<br>');
               } catch (error) {
                   console.error('Error fetching AI response:', error);
                   responseText.innerHTML = '<span class="text-red-500">Sorry, there was an error reaching the AI brain. Please make sure the backend server is running on localhost:8000.</span>';
               }
           }
       });
   </script>
   ```

## Step 3: Test It Out!

1. Make sure your backend server is running in the terminal (`uvicorn main:app --reload`).
2. Open `knowledgeDB/index.html` in your web browser.
3. Type a question like *"What do you think is a good skin routine?"* into the search bar and press **Enter**.
4. The page will send the question to the backend. `sruthiAI.py` will retrieve relevant context from the `ChromaDB_Blogs` folder, construct a prompt for Gemini, and return the answer right to your page!
