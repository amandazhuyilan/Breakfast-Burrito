#### Notes taken from a 2019 Cpp con video - [__Writing Safety Critical Automotive Software for High Perf AI Hardware__](https://tri-ad-global.slack.com/archives/G01A8UZRHN3/p1600229679002300). 

#### 1. What does it take to drive a car?
- Perception - Localization and Mapping, Scene Understanding (where is everyone else?)
- Decision Making - Movement planning (how to navigate from point A to point B)
- Monitoring - Driver state and safety monitoring
- Vehicle Control 


#### 2. Functional Safety
* ISO26262 (2011) "Absence of unreasonable risk due to hazards caused by malfunctioning behavior of electrical/electronic systems".
* "Safety" doesn't mean that the system doesn't fail - it means that the system fails safely:
    * High accuracy failure detection
    * Incorrect and late results should be considered as failures
    * Have a safe state for the system to return to
 
* Safety failure types: 
    * Systematic Failures: result of failure in design or manufacturing, or fail to follow best practises. Rate of systematic failures can be reduced through continual and rigorous process improvement.
    * Random Failures: result from random defects inherenet to process or usage condition. Rate of random failures cannot generally be reduced, focus must be on the detection and handling of random failures in the application.

#### 3. Safety Of the Intended Function (SOTIF)
* SOTIF answers the question: "_how to you tend to behave?_"
    * sensor limitations and things that can happen in the environment.
    
#### 4. How to create safe software?
* Begin with a safe and secure process
* Identify defects in software development cycle
* Use safe coding guidelines, safe and secure toolchains, or runtime or API
The above mentioned are well established for CPU, but it may not work for CPU+GPU or MPSOC or AI processor combination.

#### 5. C++ in Automative Industry
* [MISRA C++ 2008 Guideline](http://tlemp.com/download/rule/MISRA-CPP-2008-STANDARD.pdf)
* [Autosar C++ 14 Guideline](https://www.autosar.org/fileadmin/user_upload/standards/adaptive/17-03/AUTOSAR_RS_CPP14Guidelines.pdf)
