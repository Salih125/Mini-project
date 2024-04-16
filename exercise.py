class Exercise:
    name = ""
    sets = 0
    reps = 0
    exercises = []
    actualSets = []
    actualReps = []
    weights = []

    def __init__(self, name, sets, reps):
        self.name = name
        self.sets = sets
        self.reps = reps
        self.actualSets
        self.actualReps
        self.weights

        # Adds an exercise to the workout
    def addExercise(self):
        self.excercises.append(self.name)
    
    # Removes an exercise from a workout
    def removeExercise(self):
        self.exercises.remove(self.name)

    def addActualSets():
        sets = int(input('How many sets? '))
        return sets

    def addActualReps():
        reps = int(input('How many reps? '))
        return reps

    def addWeights():
        weights = float(input('How many weights? '))
        return weights