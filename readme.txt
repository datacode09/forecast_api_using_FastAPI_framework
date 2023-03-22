open VS code or any other editor of choice in the directory if the project

create virtual environment by the following command and activate it
python -m venv myenv

install required libraries by
pip install -r requirements.txt

run the FastAPI app by the command
uvicorn app:app --reload

Once the app is live on the local host, run the script.ipynb

Note:
You can change the data in the ./data directory, but the name of the column should remain the same