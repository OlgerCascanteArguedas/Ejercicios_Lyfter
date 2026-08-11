-- 1. Libros y autores
SELECT b.ID,b.Name AS Book,a.Name AS Author
FROM Books b
LEFT JOIN Authors a ON a.ID=b.Author
ORDER BY b.ID;

-- 2. Libros sin autor
SELECT b.ID,b.Name
FROM Books b
LEFT JOIN Authors a ON a.ID=b.Author
WHERE a.ID IS NULL;

-- 3. Autores sin libros
SELECT a.ID,a.Name
FROM Authors a
LEFT JOIN Books b ON b.Author=a.ID
WHERE b.ID IS NULL;

-- 4. Libros rentados
SELECT DISTINCT b.ID,b.Name
FROM Books b
INNER JOIN Rents r ON r.BookID=b.ID;

-- 5. Libros nunca rentados
SELECT b.ID,b.Name
FROM Books b
LEFT JOIN Rents r ON r.BookID=b.ID
WHERE r.ID IS NULL;

-- 6. Clientes que nunca han rentado
SELECT c.ID,c.Name,c.Email
FROM Customers c
LEFT JOIN Rents r ON r.CustomerID=c.ID
WHERE r.ID IS NULL;

-- 7. Libros con estado Overdue
SELECT b.ID,b.Name,c.Name AS Customer,r.State
FROM Rents r
INNER JOIN Books b ON b.ID=r.BookID
INNER JOIN Customers c ON c.ID=r.CustomerID
WHERE r.State='Overdue';
