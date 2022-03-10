import csv
import shutil


def main():
    originalPath = 'original/path'
    targetPath = 'target/path'
    with open('target.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            try:
                original = originalPath
                original += row[0]
                target = targetPath
                target += row[0]
                shutil.move(original, target)
            except:
                print("Error moving",row[0])
    csvfile.close()


main()

# inspired by https://docs.python.org/3/library/csv.html