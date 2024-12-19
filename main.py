import tkinter as tk
from tkinter import filedialog, messagebox
import rdflib

# Initialize the RDF graph
graph = rdflib.Graph()

# Function to upload the RDF file
def upload_rdf():
    file_path = filedialog.askopenfilename(filetypes=[("RDF Files", "*.rdf *.xml")])
    if file_path:
        try:
            graph.parse(file_path, format="xml")
            messagebox.showinfo("Success", "RDF file uploaded and parsed successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Error while parsing RDF file: {e}")

# Function to execute SPARQL query
def execute_query():
    query = query_text.get("1.0", "end-1c")
    try:
        # Execute the SPARQL query on the RDF graph
        results = graph.query(query)
        results_list = [f"Title: {row[0]}, Description: {row[1]}" for row in results]

        # Display results
        if results_list:
            results_output.config(state=tk.NORMAL)  # Enable the results display area
            results_output.delete(1.0, tk.END)  # Clear previous results
            results_output.insert(tk.END, "\n".join(results_list))
            results_output.config(state=tk.DISABLED)  # Disable editing
        else:
            messagebox.showinfo("No Results", "No results found.")
    except Exception as e:
        messagebox.showerror("Error", f"Error while executing query: {e}")

# Create the main window
root = tk.Tk()
root.title("RDF File and SPARQL Query Interface")
root.geometry("600x600")  # Increase the window size

# Create and place widgets
upload_button = tk.Button(root, text="Upload RDF File", font=("Arial", 14), command=upload_rdf)
upload_button.pack(pady=15)

query_label = tk.Label(root, text="SPARQL Query:", font=("Arial", 12))
query_label.pack(pady=5)

query_text = tk.Text(root, height=8, width=70, font=("Courier", 10))
query_text.pack(pady=5)

execute_button = tk.Button(root, text="Execute Query", font=("Arial", 14), bg="blue", fg="white", command=execute_query)
execute_button.pack(pady=15)

results_label = tk.Label(root, text="Query Results:", font=("Arial", 12))
results_label.pack(pady=5)

results_output = tk.Text(root, height=15, width=70, wrap=tk.WORD, font=("Courier", 10), state=tk.DISABLED, bg="lightyellow")
results_output.pack(pady=10)

# Run the GUI
root.mainloop()
