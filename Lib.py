D1 = {
    "Raj": 12,
    "Somya": 2,
    "Abhisek": 4,
    "Sakhi": 7,
    "Shiv": 3,
    "kartika": 5,
    "Shivam": 0,
    "Nimisha": 9,
    "Saurabh": 0,
    "Aishwarya": 2,
    "Vaishnavi": 5,
    "Rani": 10,
    "Ujwal": 1,
    "Antara": 0,
    "Akash": 3,
    "Rishi": 4,
    "Anushka": 8,
    "Nisha": 6,
    "Sandip": 7,
    "Rupali": 1
}

D2 = {
    "Python": 9,
    "Java": 3,
    "C++": 13,
    "Physics": 7,
    "Chemistry": 4,
    "Maths 1": 0,
    "Maths 2": 8,
    "Maths3": 1,
    "Geography": 3,
    "Data structure": 6,
    "OOPCG": 2,
    "Operating system": 4,
    "Data Analytics": 5,
    "Digital Finance": 2,
    "Machine Learning": 3
}


def AvgBook():
    avg = sum(D1.values()) / len(D1)
    print("Average number of books borrowed by all library members : ", avg)


def BookBorrow():
    high = max(D2, key=D2.get)
    low = min(D2, key=D2.get)
    print("Highest number of book borrowed: ", high)
    print("Lowest number of book borrowed: ", low)


def ZeroBorrow():
    zeroBorrow = 0
    for i in D1.values():
        if i == 0:
            zeroBorrow = zeroBorrow + 1
    print("Number of members with 0 borrowings:", zeroBorrow)


def FrequentBorrow():
    countFreq = {}
    for count in D2.values():
        if count in countFreq:
            countFreq[count] += 1
    else:
        countFreq[count] = 1

    maxFreq = 0
    modeCount = None
    for count, freq in countFreq.items():
        if freq > maxFreq:
            maxFreq = freq
            modeCount = count

    print("Most frequently borrowed book(s):")
    for book, count in D2.items():
        if count == modeCount:
            print(book)


AvgBook()
BookBorrow()
ZeroBorrow()
FrequentBorrow()




