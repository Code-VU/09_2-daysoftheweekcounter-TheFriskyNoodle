def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")
    handle = open(file_name)
    counts = dict()
    days = list()
    for line in handle:
        if line.startswith("From"):
            if len(line.split()) > 2:
                words=line.split()
                day=words[2]
                if day not in counts:  
                    counts[day] = 1
                else:
                    counts[day] = counts[day] +1
           
    sorted_counts=sorted(counts.items(), key=lambda x:x[1], reverse=True)
    converted_counts=dict(sorted_counts)
    print(converted_counts)

    

    



## if you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    countDayOfTheWeek()
