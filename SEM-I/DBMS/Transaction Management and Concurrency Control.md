<h1 style="color:seagreen;">Transactions</h1>

- **Set of Operations** used to perform some logical set of work.
- A transaction is made to change data in a database which can be done by inserting new data, updating the existing data, or by deleting the data that is no longer required.
- Every transaction in DBMS must maintain ACID – A (Atomicity), C (Consistency), I (Isolation), D (Durability).
- One must maintain ACID so as to ensure completeness, accuracy, and integrity of data.
- Example - Withdrawing money from the ATM.
	- The above mentioned are the set of operations done by you. But in the case of a transaction in DBMS there are three major operations that are used for a transaction to get executed in an efficient manner. These are:
	 **1. Read/ Access Data** **2. Write/ Change Data** **3. Commit**

<h2 style="color:seagreen;">Operations on Transactions</h2>

- **Read(X)** - Used to read the value of X from the database and stores it in a buffer in main memory.
- **Write(X)** - Write operation is used to write the value back to the database from the buffer.

<h2 style="color:seagreen;">Solutions to transaction failure</h2>

- Reasons - failure of hardware, software or power etc.
- Solutions - Commit and Rollback.
- **Commit** - Used to save the work done permanently. Is a **transaction control language** in SQL. Once you execute **COMMIT**, the database cannot go back to its previous state in any case.
- **Rollback** - Used to undo the work done. Operation which returns database to some previous state.

<h2 style="color:seagreen;">ACID Properties</h2>

![image](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20191121102921/ACID-Properties.jpg)
- **Atomicity**
	- Either the entire transaction takes place at once or doesn't happen at all.
	- No midway i.e. transactions do not occur partially.
	- It involves the following two operations.   
	- **Abort**: If a transaction aborts, **changes made to the database are not visible**.
	- **Commit**: If a transaction commits, changes made are visible.

- **Consistency**
	- Integrity constraints must be maintained so that the database is consistent before and after transaction.
	- It refers to the correctness of the database.

- **Isolation**
	- Isolation is the **ability of the database to concurrently process multiple transactions in a way that changes made in one does not affect the other**.
	- Example: **Cowin Portal** - When 500 slots open for a hospital, the system has to ensure that a max of 500 people can book their slots.

- **Durability**
	- This property ensures that once the transaction has completed execution, the updates and modifications to the database are stored in and written to disk and they persist even if a system failure occurs.

<h2 style="color:seagreen;">Transaction states</h2>

States through which a transaction goes during its lifetime. Tells the current situation of a transaction and also tells how we will further do the processing in the transaction.

![](https://cstaleem.com/wp-content/uploads/2021/03/States-of-Transaction-in-DBMS.png)

<h2 style="color:seagreen;">Concurrency Control</h2>

- **Concurrency Control Problem**
- When several transactions are executing concurrently without any rules and protocols, various problems may arise that can harm the data integrity of several databases. These problems are known as **Concurrency Control Problems**.
- **Concurrency control** is a procedure of managing simultaneous transactions ensuring their atomicity, isolation, consistency, and serializability.
- Concurrency control problems - Dirty read problem, Unrepeatable read problem, Phantom read problem, Lost update problem.
- To avoid concurrency problems concurrency protocols are used.
	- Lock based concurrency control protocol
	- Time-stamp concurrency control protocol
	- Validation based concurrency control protocol
	 
<h3 style="color:teal;">Lock Based concurrency protocols</h3>

n this type of protocol, any transaction cannot read or write data until it acquires an appropriate lock on it. There are **two types** of lock-Based Protocols which are explained below.
1. **Shared Lock (Read-Only) lock**
- If any transaction wants to perform **Read** operation on the data then it must acquire the shared lock on data first.
- If a transaction (say **T1**) holds an shared lock on Data(say **A**) and some other transaction (say **T2**) want to perform read operation on same data (A), then **T2 can also acquire the shared lock without waiting the unlocking of T1. It is because Read-Read is not conflict**.
2. **Exclusive Lock**
- if any transaction want to perform Read and Write both operation on same data then it must acquire the exclusive lock first.
- s