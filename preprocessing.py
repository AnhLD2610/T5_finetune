import os
import csv

def process_subfolder(subfolder_name, subfolder_path):
    rows = []
    body_path = os.path.join(subfolder_path, "test_body.csv")
    code_path = os.path.join(subfolder_path, "test_code.csv")
    title_path = os.path.join(subfolder_path, "test_title.csv")

    with open(body_path, "r", encoding='utf-8') as body_file, open(code_path, "r",encoding='utf-8') as code_file, open(title_path, "r",encoding='utf-8') as title_file:
        body_lines = body_file.readlines()
        code_lines = code_file.readlines()
        title_lines = title_file.readlines()

        for body, code, title in zip(body_lines, code_lines, title_lines):
            train_text = ' '.join(body.split()[:256]) + " <code> " + ' '.join(code.split()[:256])
            train_text = train_text.strip('"')  # Remove double quotes from the beginning and end
            title = title.strip().strip('"')  # Remove double quotes from the beginning and end of title
            rows.append([subfolder_name, train_text, title])

    return rows

def main():
    root_folder = "D:\LAB\SoTitle\data"
    train_csv_path = "test.csv"
    subfolders = [subfolder for subfolder in os.listdir(root_folder) if os.path.isdir(os.path.join(root_folder, subfolder))]

    with open(train_csv_path, "w", newline='', encoding='utf-8') as train_csv_file:
        csv_writer = csv.writer(train_csv_file)
        csv_writer.writerow(["subfolder", "train_text", "title"])

        for subfolder in subfolders:
            subfolder_path = os.path.join(root_folder, subfolder)
            rows = process_subfolder(subfolder, subfolder_path)
            csv_writer.writerows(rows)

if __name__ == "__main__":
    main()
