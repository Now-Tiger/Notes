## Security Goals
1. **Confidentiality** - Protect the confidentiality of data.
2. **Integrity** - Preserve the integrity of data.
3. **Availability** - Promote availability of data for authorized users.
4. **Non-repudiation**.
---
1. **Confidentiality**:
	- "**In law, confidentiality is a legal term that refers to the duty of an individual to refrain from sharing confidential information with others without the express consent of the other party**"
	- In cyber security Confidentiality is all about **preserving authorized restrictions on information access and disclosure, including means for protecting personal privacy and proprietary information**.
	- Also confidentiality means controlling access to files either in storage or in transit.
	- Ex. **Data encryption** - 2 factor authentication 
2. **Integrity**:
	- These measures include **file permissions and user access controls.**
	- Ensuring integrity is a matter of **version control** - **making sure only the right people can change document(s)**.
	- It also requires an **audit trail of the changes**, and a **fallback position** in case changes prove detrimental.
3. **Availability**:
	- Availability is the Cinderella of the information security as it is rarely discussed.
	- Availability means **information should be consistently and readily accessible for authorized parties**. This **involves properly maintaining the hardware and technical infrastructure and systems that hold and display the information**.

# Integrity models
These **keep data pure and trustworthy by protecting system data from intentional or accidental changes**. There are 3 goals in Integrity models.
1. **Prevent unauthorized users from making modifications to data or programs**.
2. Prevent authorized users from making improper or unauthorized modifications.
3. **Maintain internal and external consistency of data and programs**.
Ex. Balancing the batch of transactions to make sure that all the information is present and accurately accounted for.
# Availability Models
keeps data and resources available for authorized use, especially during emergencies or disasters.
There are 3 common challenges to the availability.
- DOS (Denial of Service) due to intentional attacks or undiscovered flaws in the implementation.
- Loss of information system capabilities due to natural disasters. (fire, floods, storms or earthquakes)
- Equipment failure during normal use.

# Botnets
- **A group of comprised computers controlled by a central authority, usually a hacker**.
- Collection of **independent computers each has been hacked** by a cyber-criminal i.e. hacker who uses them as a group to carry out many malicious attacks over the internet.
- each computer is remotely controlled by hacker.
- The owner/victim is completely is unware that the computer has been compromised and is a part of botnet.
- Sophisticated methods of cyber crime. hackers use them for wide range of activities, such as sending spam messages, spreading viruses, launching DOS attacks and so on.
- Goal of these attacks is financial gain, which is proportional to the size of botnet.
- Botnets sometimes called as "Zombies" because each computer follows orders of their hacker/owner and hacker is called as "Botmaster".
- Some botnets might have few hundred computers, while others may have thousands or even a million computers.

# DOS - Denial-of-Service Attack
- **A type of attack used to prevent legitimate users from accessing services or resources**.
- In a denial-of-service attack, **a hacker can prevent authorized users from accessing resources and services.** Eg. Access of websites, using mail, video conferencing, banking services and so on.
- Hacker can target computers or network connections.
- Common way performing DOS attack on a website is basically **flooding** target **website with large number of information requests**.  This will prevent other users from accessing it, as each website can accept only a limited number of requests.

# HACKTIVISM
- Modern way of protest in which savvy programmers use their hacking skills to fight back against the social and political injustice.
- Though **non-violent**, most acts of hacktivism are illegal.
- Some view these hacktivists as a heroic vigilantes who use their tech wizardry to defend the public good.
- In recent years, a loosely-organized group of hacktivists called "**Anonymous**", whose members attend demonstrations wearing signature **Guy Fawkes masks**, **has pulled off a series of especially infamous hacks**. Here are a few highlights.
- Few cases of Hacktivism
	- Aaron Swartz
	- The Jester
	- Barrett Brown

# Cyber Espionage
"The practice of spying or obtaining secrets from rivals or enemies for military, political, or business advantage."
Simply, unauthorized and usually criminal access to confidential systems and information for the purpose of gaining commercial or political advantage.

# Threat Modeling
Threat modeling is a structured process with these objectives: **identify security requirements, pinpoint security threats and potential vulnerabilities, quantify threat and vulnerability criticality, and prioritize remediation methods.**
High level view - **Assessing the security risk of a software system from an adversary's perspective**.
## $GOALS$
1. Understand threats to guard against during requirement analysis.
2. Provide basis for which security mechanism to include during design.
3. Verify security of system design.
4. Provide basis for secure implementation practices.
5. Provide basis for testing the system security after implementation.
## How threat modeling works / Process:
- **Works by identifying types of threats and agents** that can cause to an application or computer system. It adopts the perspective of malicious hacker to see how much damage they could do.
- When conducting threat modeling, organizations perform thorough analysis of the software architecture, business context, and other artifacts.
- This process enables a deeper understanding and discovery of important aspects of the system.
- Generally organizations conduct threat modeling during the **design/definition stage** of a new application to help developers to find the vulnerabilities and become aware of security.
- Generally developers perform threat modeling in four steps:
	- Diagram - What are we building?
	- Identify threats - What could go wrong?
	- Mitigate - What are we doing to defend against the threats?
	- Validate - Have we acted on each of the previous steps?
---
# $Unit 3$
# Multi-Lateral Security:
- Multilateral Security means **taking into consideration the security requirements of all parties involved**. **It also means considering all involved parties as potential attackers.**
- This is especially important for open communication systems, as one cannot expect the various parties to trust each other.
- One of the main aims of security of any organization is not only prevent information "down" a hierarchal order(Multilevel) but also to stop the leak “across” the departments.

There are three different models of how to implement access control and information flow control in multilateral security. These are;
1. Compartmentation and the lattice Model
2. Chinese wall model
3. British Medical Association (BMA) Model.

## Steps for Integrating security into application development
- Organizations spends resources, time & money to protect their network parameters from internet borne threats and hackers. But **no matter how good a defense may be, it usually falls short in addressing the vulnerabilities inside the network at the application layer.**
- Recent research findings indicate that the application layer is one of the highest-risk areas and where the most potential damage can occur, either through insider targets or lack of protection. As a result, confidential company information can be exposed, resulting in a harm to a company, its customers and its reputation.
### Areas to considers when integrating security in an application
1. **Initial Review**
- Which will allow the security team to asses initial risks.
- security team will work with the development team to gain an understanding of following things:

2. **Definition Phase: Threat modeling**
- Threat modeling is the practice of **working with developers to identify critical areas of applications** dealing with sensitive information.
- The model is used to map information flow and identify critical areas of the application's infrastructure that require added security attention.

3. **Design Phase**
- Application design reviews are an important step in identifying potential security risks at the early development stage.
