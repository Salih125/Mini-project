from exercise import Exercise

class Workout():
    name = ""
    workouts = []
    workoutsF = open('workouts.txt', 'a')

    def __init__(self, name):
        self.name = name
        
    # Creates a workout and add´s it to the workouts list
    def createWorkout(self):
        self.workoutsF.write(self.name)
        #self.workouts.append(self.name)
    
    # Removes workout from the list
    def removeWorkout(self):
        self.workouts.remove(self.name)
