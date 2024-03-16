# Incident Report: Login Service Outage
## Issue Summary

 - **Duration:** 2 hours 15 minutes (from 14:30 PST on 2024-03-15 to 16:45 PST on 2024-03-15)
 - **Impact:** The login service outage prevented users from accessing the company's internal applications. Approximately 80% of users were affected.
 - **Root Cause:** Database connection pool exhaustion due to a bug in a recently deployed code update.

## Timeline

- **14:30 PST:** Login service alerts triggered due to a surge in failed login attempts.
![Man throwing a computer](https://www.uuss.org/wp-content/uploads/2015/03/funny-gif-man-throws-monitor.gif)
- **14:32 PST:** An engineer on-call identified the alert and began investigating. Initial suspicion was a potential DDoS attack.
- **14:40 PST:** Investigation shifted towards login service health checks after no evidence of a DDoS attack was found.
- **14:55 PST:** Database team was notified due to concerns about potential database connectivity issues.
- **15:10 PST:** Database logs revealed high connection pool usage and timeouts.
- **15:20 PST:** The incident was escalated to the development team responsible for the recent code update.
- **15:30 PST:** Code review identified a bug causing excessive database connection requests.
- **15:45 PST:** A hotfix was deployed to address the bug.
![Hot fix](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMDE4dXk4cm9jYXVqZjhvZ3Nhemhnam1yMWtsanhmend5Mjk3eGl6dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/AvMJCeu1EMmhG/giphy.gif)
- **16:30 PST:** Login service functionality recovered.
- **16:45 PST:** All systems confirmed operational.
 
- ![It works](https://media.giphy.com/media/111ebonMs90YLu/giphy.gif)

## Root Cause and Resolution

The root cause of the outage was a bug in a recently deployed code update. The update introduced an inefficiency that caused the login service to make excessive database connection requests. This overwhelmed the connection pool, leading to connection timeouts and ultimately login failures.

The resolution involved identifying the bug in the code and deploying a hotfix. The hotfix addressed the inefficiency and restored normal database connection usage patterns.

## Corrective and Preventative Measures

 - **Improve code review processes:** Implement stricter code reviews to identify potential connection pool exhaustion issues before deployment.
 - **Increase connection pool size (temporary):** While a permanent fix is developed, increase the database connection pool size to handle unexpected spikes in requests.
 - **Implement unit testing for connection management:** Develop unit tests that simulate user traffic and validate connection pool behavior under load.
 - **Monitor connection pool usage:** Implement robust monitoring for database connection pool usage to identify potential problems before they cause outages.


This incident highlights the importance of thorough code review and proactive monitoring. By implementing the corrective and preventative measures outlined above, we can minimize the risk of similar incidents occurring in the future.