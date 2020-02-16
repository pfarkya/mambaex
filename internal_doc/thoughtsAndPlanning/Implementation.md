## First Phase Development Plan

#### Multi Server Class

> Working
Holds multiple server instance

#### Server Class Methods
> Working
Handling creation of App Stack and HTTP Handler
`get`
`put`
`patch`
`use`
`post`
`delete`
`listen`
`stop`
For now we will not handle multiple function and pluggable router.


#### Request Class Method Fully instantiated gives a single request object
> Working
Responsible to give access to the request object with parsed manner
`headers`
`method`
`body` json/utf-8 text/html/buffered read part only
`read` <- `r.read`

#### Response Class
>  Working
Responsible for response object handling
`status`
`send`

#### Context class
>  Working
Responsible for ctx.raw, ctx.req and ctx.res  object handling for making availability of raw content

#### Helping Class
> Working making some helping function to be used for various works within other classes


#### Utils class
> Which might need
`static`


#### Router class
> not require for first shot


#### Working

While we have a appstack to maintained per instance which will be processed and served while we are serving request
