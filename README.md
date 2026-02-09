PCA: Financial Inclusion in East Africa.

What is this?
This project is a deep dive into who has access to banking in Kenya, Rwanda, Tanzania, and Uganda. I used Principal Component Analysis (PCA) to take a complex list of 33 demographic features and boil them down to the ones that actually matter.

Key Features
From-Scratch PCA: Built the math (Covariance, Eigendecomposition) without using high-level libraries like scikit-learn.

Smart Selection: The code automatically picks enough components to keep 95% of the original data's information.

Performance: Optimized to process over 23,000 rows of African survey data in milliseconds.

Setup & Usage
Install: pip install -r requirements.txt

The Library: I’ve included pca_lib.py, which is my own custom tool for this analysis.

Run it:

Python
from pca_lib import PCA_Analysis_Tool
pca = PCA_Analysis_Tool(n_components=2)
pca.fit(X_standardized)
reduced_data = pca.transform(X_standardized)
How to finalize your submission:
Download from Colab:

The Notebook: File -> Download -> .ipynb.

The Library: Click the folder icon on the left of Colab, right-click pca_lib.py, and hit Download.

GitHub Upload:

Go to your GitHub repo.

Click Add file -> Upload files.

Drag in your Notebook, pca_lib.py, requirements.txt, and Train.csv.

The README:

Open the README.md on GitHub, click the pencil icon, and paste the "Humanized" text above.

Save/Commit.
