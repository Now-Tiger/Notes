- Software architecture is simply, the **organization of system**.
- This organization includes all components, how they interact and provides an explanation of they behave with each other.

# Software Architecture Design
- Using **programming knowledge to plan the high-level view/design of software** so that details can be implemented later and focus on bigger picture and begin preparing prototyping.

# 5 steps to design software architecture
1. **Requirements** - Clear Understanding of requirements
	- Every design/project has both functional and non-functional requirements. These requirements guide your software architecture along and allow you to finish up the project with and end product that stakeholders are requiring. 
	- Without clear understanding of requirements from the beginning, different risks gets introduced, wrong requirements can be expensive, redundant when developing the project.
	- **Visuals: Mind Mapping** - Gain better understanding through visuals. Mind mapping is effective way to do this. Sketch requirements at a "Helicopter View" first.
	- Within mind map plot requirements and connect those which are correlated.

2. **Components** - Think about each components.
	- Without getting too far ahead of yourself thinking about implementation, you'll need to find out **which requirements pose significant challenges** to your design/project plan. Some requirements may actually be impossible to under certain assumptions.
	- Start with a **"Perfect world"** - What would your design look like if you create it perfectly ?
	- **Drafting** - Consider and document the implications of your requirements. Start a working draft with your team and develop it gradually. 
	- **Don't expect final results at first** - Wait and design the final architecture later: In all likelihood, your architecture planning will change throughout this process, so don’t expect the first draft to resemble the final result.

3. **Divide & Conquer** - Divide your architecture into slices.
	-  Dividing your architecture into slices can help you craft this plan in a way that it delivers end product to the users and you can properly plan your use of development resources.
	- Cake(layered) slicing example related with software architecture slicing - 1. Vertical 2. Horizontal slicing.
	- **Vertical slicing** - Slicing cake vertically creates stories centered around individual features.
	- **Horizontal slicing** - Reveals individual components.
	- **Agile** focuses on vertical slices, allowing teams to quickly develop the product. Vertical slice of an e-commerce website might be the "Check-Out" process. In "checkout" vertical slice you can see the data layer storing the information, then middle layer for APIs, and at top layer is User-Interface that shoppers/users see. With vertical slices use can decide with features to deliver.

 4. **Prototype** - Prototyping 
	 - Allows you to fail fast and early - Providing quick feedback and allowing you to discover your proof-of-concept. Helps validating and checking your assumptions.
	 - First few iterations in your prototyping are never perfect and no final iteration will be completely perfect either.
	 - Prototyping Phases -
	 - **Book keeping** - Keep careful revision history. If you don't document what you learn from prototyping, you run the risk of repeating your mistakes. Write thorough documentation of your design decisions and changes you make/made along the way.
	 - **Single source of truth** - You don't want multiple changes and different versions to track your progress, so set up robust version control focused on a single source of your documentation.
	 - **Diagram prototypes** - visualization helps manage the prototype changes and understand difference between each version.

5. **Non-functional requirements** - Identify & quantify non-functional requirements
	 -  In addition to the functional requirements, you’ll have non-functional requirements to take into consideration. They define system's characteristics.
	 - Often known as **high-level quality requirements** for entire project, also not always.
	 - Since your non-functional requirements play a role in shaping your design, you can’t avoid defining them. Here are some other requirements you may want to consider.
	 - **Performance** - How well your entire system performs as well as individual slices and layers.
	 - **Scalability** - Current and future potential to scale your sytem.
	 - **Portability**
	 - **Extensibility**
	 - **Compliance** 