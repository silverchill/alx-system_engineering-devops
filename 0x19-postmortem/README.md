# Issue Summary:

## Duration: 
The outage occurred started on May 10, 2024 11:00 AM to May 10, 2024 3:00 PM (UTC).
## Impact:
 The web application experienced complete unavailability, affecting 75% of active users. Users attempting to access the service encountered connection errors and timeouts.
## Root Cause:

The root cause of the outage was identified as a misconfiguration in the load balancer settings, leading to an overload on one of the application servers.

# Timeline:

10:00 AM (UTC): Issue detected by monitoring alerts indicating a spike in server response times.
10:05 AM (UTC): Engineering team notified through automated alerting systems.
10:10 AM (UTC): Initial investigation focused on server health metrics and database performance.
10:30 AM (UTC): Incorrectly assumed database overload as the root cause due to high CPU usage.
11:00 AM (UTC): Incident escalated to senior engineering team members for further analysis.
11:30 AM (UTC): Load balancer misconfiguration identified as the primary suspect.
12:00 PM (UTC): Load balancer settings adjusted to distribute traffic evenly across application servers.
1:30 PM (UTC): Service fully restored as traffic stabilized across servers.

# Root Cause and Resolution:

The misconfiguration in the load balancer caused uneven distribution of traffic, leading to overloading of one application server. This resulted in increased response times and eventual unavailability of the service.

To resolve the issue, the load balancer settings were corrected to evenly distribute incoming traffic across all available application servers. This restored balance and stability to the system, allowing it to handle user requests effectively.

# Corrective and Preventative Measures:

Load Balancer Configuration Review: Conduct a thorough review of load balancer settings to ensure proper distribution of traffic.
Automated Health Checks: Implement automated health checks to promptly detect and alert on any misconfigurations or anomalies in system components.
Enhanced Monitoring: Enhance monitoring systems to provide deeper insights into server performance metrics, enabling quicker identification of issues.
Regular Training: Provide regular training sessions for engineering teams to improve troubleshooting skills and familiarity with system components.

# Conclusion:

The outage was a result of a misconfiguration in the load balancer, leading to service unavailability for a significant portion of users. By promptly identifying and correcting the issue, the service was restored within a few hours. Moving forward, implementing corrective measures and enhancing monitoring will help prevent similar incidents and ensure the stability and reliability of the platform:
