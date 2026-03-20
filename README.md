 🚀 AI-Based Parametric Insurance for Gig Workers
 📌 Problem Statement

Gig workers such as delivery partners are highly vulnerable to income loss due to external disruptions like heavy rain, heatwaves, and pollution. Existing insurance systems are slow, paper-based, prone to fraud, and not real-time. There is no instant, automated, and fraud-resistant system to protect their daily income.

💡 Solution Overview

This project is an AI-powered parametric insurance platform that calculates premiums dynamically, detects real-world disruptions using APIs, triggers instant payouts, and prevents fraud using behavioral logic.

⚙️ Key Features

🧠 AI-Based Premium Calculation
Premium is calculated dynamically based on income and location risk.

🌍 Real-Time Event Detection
Integrated with OpenWeather API to detect actual weather conditions.

⚡ Zero-Touch Claims
No manual claim process. Automatic payout is triggered when disruption occurs.

🔐 Fraud Detection System
Prevents duplicate claims and blocks repeated claim attempts.

🚨 Adversarial Defense & Anti-Spoofing Strategy

Fraudsters may attempt to fake GPS locations, trigger multiple claims, or exploit system vulnerabilities.

🛡️ Defense Strategy

- Duplicate claim prevention using system-level tracking  
- Real-world validation using OpenWeather API  
- Location consistency validation (conceptual extension)  
- Behavioral pattern analysis to detect abnormal activity  
- Cooldown mechanism to limit frequent claims  
- Detection of fraud rings based on repeated patterns  

The system ensures fairness by blocking only suspicious patterns while allowing genuine claims.


🏗️ System Architecture

User → Register → Dashboard → Trigger Event → API Verification → Payout  
                                                                     ↓  
                                                       Fraud Detection Layer  

🧪 Tech Stack

Frontend: HTML, CSS, JavaScript  
Backend: Flask (Python)  
API: OpenWeather API  
Visualization: Chart.js  

📊 Workflow

1. User registers with name, city, and income  
2. System calculates premium  
3. User triggers disruption (Rain / Heat / Pollution)  
4. API verifies real condition  
5. System processes payout  
6. Fraud detection prevents misuse  

🚀 Future Enhancements

Live GPS tracking  
Machine learning-based fraud detection  
Mobile app integration  
Advanced analytics dashboard  
Blockchain-based claim validation  

🎯 Impact

Protects gig workers' income  
Eliminates paperwork  
Reduces fraud  
Enables real-time insurance  

🏁 Conclusion

This system introduces a next-generation parametric insurance model that is instant, transparent, fraud-resistant, and scalable.
