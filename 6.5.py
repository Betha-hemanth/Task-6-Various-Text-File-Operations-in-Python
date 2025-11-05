File: feedback.txt

The service was very good.
I liked the delivery speed.
Could improve the packaging.
Excellent customer support!
Average experience.



f = open("feedback.txt", "r")
feedbacks = f.readlines()
f.close()

longest = max(feedbacks, key=len)
summary = "Total Feedback: " + str(len(feedbacks)) + "\nLongest Feedback: " + longest

f = open("feedback_summary.txt", "w")
f.write(summary)
f.close()
print("Feedback summary saved.")

