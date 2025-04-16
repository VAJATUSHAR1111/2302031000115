import pandas as pd

# Sample student data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Math': [88, 76, 93, 85, 91],
    'Science': [92, 81, 87, 90, 89],
    'English': [84, 79, 85, 88, 90]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Add average grade column
df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1)

# Find top performer
top_student = df.loc[df['Average'].idxmax()]

print("Student Grades Summary:")
print(df)
print("\nTop Performer:")
print(top_student)
