class WorkoutData:

    # Workout name
    name = ''

    # Adds workout to workouts file
    def addWorkout(name):
        data = open('workouts.txt', 'a')
        data.write(name)
        data.close()

    # Removes workout from workouts file 
    def removeWorkout(name):
        # Open file in read mode to save the lines
        data = open('workouts.txt', 'r')
        lines = data.readlines()
        data.close()

        # Open file in write mode to loop through each lines
        # and avoids name 
        data = open('workouts.txt', 'w')
        for line in lines:
            if line.rstrip() != name:
                data.write(line)
        data.close()
        
    # Reads workouts file
    def readWorkouts():
        data = open('workouts.txt', 'r')
        read = data.read()
        data.close()
        return read