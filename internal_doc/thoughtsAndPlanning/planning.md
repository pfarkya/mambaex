 ### Aim for Creating this Project
Providing an RESTFul open source server framework (similiar to express) with powerful functionality.

### Design for the project
There are 3 part of design 1) Basic Functionality 2) Advance Functionality 3) Utility Helper Functionality

#### Basic Functionality
- Server Creation
- Request
- Response
- Middleware

#### Advance Functionality
- Routers
- template engine support

#### Utility Helper Functionality
- bodyParser
- urlParser

### Basic Architecture for the project
Simple architecture in words :-
There is a server creation with named singleton Class (called as APP/server) with providing wrappers of REST APIs (include Methods).
Which will create an APP Stack which will be call subroutines (called as middleware), middleware will be passed with 3 PARAMs
Request, Response and next Handler.

### Planing to Execute this project

Will start with proper documention, packaging and publishing of this Framework (processed by CI CD model)
Open Source model as contribute guideline, issue guideline, Linsensing , Pull Request guildlines, Commit Message checks all things needs to include.
