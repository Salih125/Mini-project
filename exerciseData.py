class ExerciseData:

    # Exercise name
    name = ''

    # Adds exercise to exercises file
    def addExercise(name):
        data = open('exercises.txt', 'a')
        data.write(name)
        data.close()

    # Removes exercise from exercises file
    def removeExercise(name):
        # Open file in read mode to save the lines
        data = open('exercises.txt', 'r')
        lines = data.readlines()
        data.close()

        # Open file in write mode to loop through each lines
        # and avoids name 
        data = open('exercises.txt', 'w')
        for line in lines:
            if line.rstrip() != name:
                data.write(line)
        data.close()

    # Reads exercises file
    def readExercises():
        data = open('exercises.txt', 'r')
        read = data.read()
        data.close()
        return read