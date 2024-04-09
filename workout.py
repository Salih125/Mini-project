from exercise import Exercise

class Workout():
    name = ""
    exercises = []
    workouts = []

    def __init__(self, name):
        self.name = name
        
    # Creates a workout and add´s it to the workouts list
    def createWorkout(self):
        self.workouts.append(Workout)

    # Adds an exercise to the workout
    def addExercise(self):
        self.excercises.append(Exercise)
    
    # Removes an exercise from a workout
    def removeExercise(self):
        self.exercises.remove(Exercise)