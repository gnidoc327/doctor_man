a"""students = [
 ("김한성", [{"C강의", "A+"}, {"창의적설계", "F"}, {"네트워크", "D"}]),
 ("고은진", [{"C강의", "C+"}, {"창의적설계", "A+"}]),
 ("박시현", [{"C강의", "B+"}, {"창의적설계", "B"}])
]

scores = [
 {"A+": "4.5"},
 {"A": "4"},
 {"B+": "3.5"},
 {"B": "3"},
 {"C+": "2.5"},
 {"C": "2"},
 {"D+": "1.5"},
 {"D": "1"},
 {"F": "0"}
]

lectures = [
 {"C강의": "3"},
 {"창의적설계": "2"},
 {"네트워크":"1"}
]

students_number = [
 {"김한성":"0"},
 {"고은진": "1"},
 {"박시현": "2"},
]

def showScore(students_input):
 return (int(scores[str(students[(students_number[students_input])]['C강의'])])*int(lectures['C강의'])
         +int(scores[str(students[(students_number[students_input])]['창의적설계'])])*int(lectures['창의적설계'])
         +int(scores[str(students[(students_number[students_input])]['네트워크'])])*int(lectures['네트워크'])) / 6


showScore("김한성")
showScore("고은진")
showScore("박시현")"""

