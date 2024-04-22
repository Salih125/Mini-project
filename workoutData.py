class WorkoutData:

    # Workout name
    name = ''

    # Workouts list
    workouts = []

    def __init__(self, name):
        self.name = name

    # Adds workout to workouts file
    def addWorkout(self, name):
        self.workouts.append(name)

        data = open('workoutsFile.txt', 'a')
        data.write(name)
        data.write('\n')
        data.close()

    # Removes workout from workouts file 
    def removeWorkout(self, name):
        # Open file in read mode to save the lines
        data = open('workoutsFile.txt', 'r')
        lines = data.readlines()
        data.close()

        # Open file in write mode to loop through each lines
        # and avoids name 
        data = open('workoutsFile.txt', 'w')
        for line in lines:
            if line.rstrip() != name:
                data.write(line)
        data.close()
        
    # Reads workouts file
    def readWorkouts():
        data = open('workoutsFile.txt', 'r')
        read = data.readlines()
        data.close()