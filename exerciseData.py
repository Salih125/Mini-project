class ExerciseData:

    # Exercise name
    name = ''
    sets = 0
    reps = 0
    weight = 0

    # Exercises list
    exercisesList = []
    actualSetsList = []
    actualRepsList = []
    weightsList = []

    def __init__(self, name):
        self.name = name
        self.exercisesList
        self.actualSetsList
        self.actualRepsList
        self.weightsList

    # Adds exercise to exercises file
    def addExercise(self, name):
        self.exercisesList.append(name)

        data = open('exercisesFile.txt', 'a')
        data.write(name)
        data.write('\n')
        data.close()

    # Removes exercise from exercises file
    def removeExercise(self, name):
        #self.exercisesList.remove(name)

        # Open file in read mode to save the lines
        data = open('exercisesFile.txt', 'r')
        lines = data.readlines()
        data.close()

        # Open file in write mode to loop through each lines
        # and avoids name 
        data = open('exercisesFile.txt', 'w')
        for line in lines:
            if line.rstrip() != name:
                data.write(line)
        data.close()

    # Reads exercises file
    def readExercises():
        data = open('exercisesFile.txt', 'r')
        read = data.read()
        data.close()
        return read
    
    # Adds
    def addActualSets(self, sets):
        self.actualSetsList.append(sets)

        data = open('setsFile.txt', 'a')
        data.write(sets)
        data.write('\n')
        data.close()
        
    def addActualReps(self, reps):
        self.actualRepsList.append(reps)

        data = open('repsFile.txt', 'a')
        data.write(reps)
        data.write('\n')
        data.close()

    def addWeights(self, weight):
        self.weightsList.append(weight)

        data = open('weightsFile.txt', 'a')
        data.write(weight)
        data.write('\n')
        data.close()

    