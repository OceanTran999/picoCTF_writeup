![chal](https://github.com/user-attachments/assets/a7f7b18b-e1bc-4c6d-81b3-c80c3c031995)


Using `psql` command to access to the SQL server of the target. List the database with `\l` command.

![access1](https://github.com/user-attachments/assets/96562ae9-62c5-4988-9b41-cf9e8f414b8c)


Access the **pico** database with `\c pico` command.

![access2](https://github.com/user-attachments/assets/8cb8ccff-059f-4424-8e2b-ed42c9cef18d)


We can see that there is a `flags` column, read the content of this column but it seems there's nothing useful information.

![access3](https://github.com/user-attachments/assets/bce92344-770b-44bf-a7ba-75c0c8afd3d8)


To get the flag, we will extract using the `SELECT` command of the `flags` column.

![flag](https://github.com/user-attachments/assets/d5eb775f-e8a4-43e5-9c8a-09e23246796c)
