import os
import pandas as pd
import random
import string

alphabet = string.ascii_uppercase
alphabetList = []
for eachLetter in alphabet:
    alphabetList.append(eachLetter)

file = ""

orgionalFile = pd.read_csv("")

rowNumbers = len(orgionalFile.index)

firstNames=['Liam','Noah','Oliver','Elijah','James','William','Benjamin','Lucas','Henry','Theodore','Jack','Levi','Alexander','Jackson','Mateo','Daniel','Michael','Mason','Sebastian','Ethan','Logan','Owen','Samuel','Jacob','Asher','Aiden','John','Joseph','Wyatt','David','Leo','Luke','Julian','Hudson','Grayson','Matthew','Ezra','Gabriel','Carter','Isaac','Jayden','Luca','Anthony','Dylan','Lincoln','Thomas','Maverick','Elias','Josiah','Charles','Caleb','Christopher','Ezekiel','Miles','Jaxon','Isaiah','Andrew','Joshua','Nathan','Nolan','Adrian','Cameron','Santiago','Eli','Aaron','Ryan','Angel','Cooper','Waylon','Easton','Kai','Christian','Landon','Colton','Roman','Axel','Brooks','Jonathan','Robert','Jameson','Ian','Everett','Greyson','Wesley','Jeremiah','Hunter','Leonardo','Jordan','Jose','Bennett','Silas','Nicholas','Parker','Beau','Weston','Austin','Connor','Carson','Dominic','Xavier','Jaxson','Jace','Emmett','Adam','Declan','Rowan','Micah','Kayden','Gael','River','Ryder','Kingston','Damian','Sawyer','Luka','Evan','Vincent','Legend','Myles','Harrison','August','Bryson','Amir','Giovanni','Chase','Diego','Milo','Jasper','Walker','Jason','Brayden','Cole','Nathaniel','George','Lorenzo','Zion','Luis','Archer','Enzo','Jonah','Thiago','Theo','Ayden','Zachary','Calvin','Braxton','Ashton','Rhett','Atlas','Jude','Bentley','Carlos','Ryker','Adriel','Arthur','Ace','Tyler','Jayce','Max','Elliot','Graham','Kaiden','Maxwell','Juan','Dean','Matteo','Malachi','Ivan','Elliott','Jesus','Emiliano','Messiah','Gavin','Maddox','Camden','Hayden','Leon','Antonio','Justin','Tucker','Brandon','Kevin','Judah','Finn','King','Brody','Xander','Nicolas','Charlie','Arlo','Emmanuel','Barrett','Felix','Alex','Miguel','Abel','Alan','Beckett','Amari','Karter','Timothy','Abraham','Jesse','Zayden','Blake','Alejandro','Dawson','Tristan','Victor','Avery','Joel','Grant','Eric','Patrick','Peter','Richard','Edward','Andres','Emilio','Colt','Knox','Beckham','Adonis','Kyrie','Matias','Oscar','Lukas','Marcus','Hayes','Caden','Remington','Griffin','Nash','Israel','Steven','Holden','Rafael','Zane','Jeremy','Kash','Preston','Kyler','Jax','Jett','Kaleb','Riley','Simon','Phoenix','Javier','Bryce','Louis','Mark','Cash','Lennox','Paxton','Malakai','Paul','Kenneth','Nico','Kaden','Lane','Kairo','Maximus','Omar','Finley','Atticus','Crew','Brantley','Colin','Dallas','Walter','Brady','Callum','Ronan','Hendrix','Jorge','Tobias','Clayton','Emerson','Damien','Zayn','Malcolm','Kayson','Bodhi','Bryan','Aidan','Cohen','Brian','Cayden','Andre','Niko','Maximiliano','Zander','Khalil','Rory','Francisco','Cruz','Kobe','Reid','Daxton','Derek','Martin','Jensen','Karson','Tate','Muhammad','Jaden','Joaquin','Josue','Gideon','Dante','Cody','Bradley','Orion','Spencer','Angelo','Erick','Jaylen','Julius','Manuel','Ellis','Colson','Cairo','Gunner','Wade','Chance','Odin','Anderson','Kane','Raymond','Cristian','Aziel','Prince','Ezequiel','Jake','Otto','Eduardo','Rylan','Ali','Cade','Stephen','Ari','Kameron','Dakota','Warren','Ricardo','Killian','Mario','Romeo','Cyrus','Ismael','Russell','Tyson','Edwin','Desmond','Nasir','Remy','Tanner','Fernando','Hector','Titus','Lawson','Sean','Kyle','Elian','Corbin','Bowen','Wilder','Armani','Royal','Stetson','Briggs','Sullivan','Leonel','Callan','Finnegan','Jay','Zayne','Marshall','Kade','Travis','Sterling','Raiden','Sergio','Tatum','Cesar','Zyaire','Milan','Devin','Gianni','Kamari','Royce','Malik','Jared','Franklin','Clark','Noel','Marco','Archie','Apollo','Pablo','Garrett','Oakley','Memphis','Quinn','Onyx','Alijah','Baylor','Edgar','Nehemiah','Winston','Major','Rhys','Forrest','Jaiden','Reed','Santino','Troy','Caiden','Harvey','Collin','Solomon','Donovan','Damon','Jeffrey','Kason','Sage','Grady','Kendrick','Leland','Luciano','Pedro','Hank','Hugo','Esteban','Johnny','Kashton','Ronin','Ford','Mathias','Porter','Erik','Johnathan','Frank','Tripp','Casey','Fabian','Leonidas','Baker','Matthias','Philip','Jayceon','Kian','Saint','Ibrahim','Jaxton','Augustus','Callen','Trevor','Ruben','Adan','Conor','Dax','Braylen','Kaison','Francis','Kyson','Andy','Lucca','Mack','Peyton','Alexis','Deacon','Kasen','Kamden','Frederick','Princeton','Braylon','Wells','Nikolai','Iker','Bo','Dominick','Moshe','Cassius','Gregory','Lewis','Kieran','Isaias','Seth','Marcos','Omari','Shane','Keegan','Jase','Asa','Sonny','Uriel','Pierce','Jasiah','Eden','Rocco','Banks','Cannon','Denver','Zaiden','Roberto','Shawn','Drew','Emanuel','Kolton','Ayaan','Ares','Conner','Jalen','Alonzo','Enrique','Dalton','Moses','Koda','Bodie','Jamison','Phillip','Zaire','Jonas','Kylo','Moises','Shepherd','Allen','Kenzo','Mohamed','Keanu','Dexter','Conrad','Bruce','Sylas','Soren','Raphael','Rowen','Gunnar','Sutton','Quentin','Jaziel','Emmitt','Makai','Koa','Maximilian','Brixton','Dariel','Zachariah','Roy','Armando','Corey','Saul','Izaiah','Danny','Davis','Ridge','Yusuf','Ariel','Valentino','Jayson','Ronald','Albert','Gerardo','Ryland','Dorian','Drake','Gage','Rodrigo','Hezekiah','Kylan','Boone','Ledger','Santana','Jamari','Jamir','Lawrence','Reece','Kaysen','Shiloh','Arjun','Marcelo','Abram','Benson','Huxley','Nikolas','Zain','Kohen','Samson','Miller','Donald','Finnley','Kannon','Lucian','Watson','Keith','Westin','Tadeo','Sincere','Boston','Axton','Amos','Chandler','Leandro','Raul','Scott','Reign','Alessandro','Camilo','Derrick','Morgan','Julio','Clay','Edison','Jaime','Augustine','Julien','Zeke','Marvin','Bellamy','Landen','Dustin','Jamie','Krew','Kyree','Colter','Johan','Houston','Layton','Quincy','Case','Atreus','Cayson','Aarav','Darius','Harlan','Justice','Abdiel','Layne','Raylan','Arturo','Taylor','Anakin','Ander','Hamza','Otis','Azariah','Leonard','Colby','Duke','Flynn','Trey','Gustavo','Fletcher','Issac','Sam','Trenton','Callahan','Chris','Mohammad','Rayan','Lionel','Bruno','Jaxxon','Zaid','Brycen','Roland','Dillon','Lennon','Ambrose','Rio','Mac','Ahmed','Samir','Yosef','Tru','Creed','Tony','Alden','Aden','Alec','Carmelo','Dario','Marcel','Roger','Ty','Ahmad','Emir','Landyn','Skyler','Mohammed','Dennis','Kareem','Nixon','Rex','Uriah','Lee','Louie','Rayden','Reese','Alberto','Cason','Quinton','Kingsley','Chaim','Alfredo','Mauricio','Caspian','Legacy','Ocean','Ozzy','Briar','Wilson','Forest','Grey','Joziah','Salem','Neil','Remi','Bridger','Harry','Jefferson','Lachlan','Nelson','Casen','Salvador','Magnus','Tommy','Marcellus','Maximo','Jerry','Clyde','Aron','Keaton','Eliam','Lian','Trace','Douglas','Junior','Titan','Cullen','Cillian','Musa','Mylo','Hugh','Tomas','Vincenzo','Westley','Langston','Byron','Kiaan','Loyal','Orlando','Kyro','Amias','Amiri','Jimmy','Vicente','Khari','Brendan','Rey','Ben','Emery','Zyair','Bjorn','Evander','Ramon','Alvin','Ricky','Jagger','Brock','Dakari','Eddie','Blaze','Gatlin','Alonso','Curtis','Kylian','Nathanael','Devon','Wayne','Zakai','Mathew','Rome','Riggs','Aryan','Avi','Hassan','Lochlan','Stanley','Dash','Kaiser','Benicio','Bryant','Talon','Rohan','Wesson','Joe','Noe','Melvin','Vihaan','Zayd','Darren','Enoch','Mitchell','Jedidiah','Brodie','Castiel','Ira','Lance','Guillermo','Thatcher','Ermias','Misael','Jakari','Emory','Mccoy','Rudy','Thaddeus','Valentin','Yehuda','Bode','Madden','Kase','Bear','Boden','Jiraiya','Maurice','Alvaro','Ameer','Demetrius','Eliseo','Kabir','Kellan','Allan','Azrael','Calum','Niklaus','Ray','Damari','Elio','Jon','Leighton','Axl','Dane','Eithan','Eugene','Kenji','Jakob','Colten','Eliel','Nova','Santos','Zahir','Idris','Ishaan','Kole','Korbin','Seven','Alaric','Kellen','Bronson','Franco','Wes','Larry','Mekhi','Jamal','Dilan','Elisha','Brennan','Kace','Van','Felipe','Fisher','Cal','Dior','Judson','Alfonso','Deandre','Rocky','Henrik','Reuben','Anders','Arian','Damir','Jacoby','Khalid','Kye','Mustafa','Jadiel','Stefan','Yousef','Aydin','Jericho','Robin','Wallace','Alistair','Davion','Alfred','Ernesto','Kyng','Everest','Gary','Leroy','Yahir','Braden','Kelvin','Kristian','Adler','Avyaan','Brayan','Jones','Truett','Aries','Joey','Randy','Jaxx','Jesiah','Jovanni','Azriel','Brecken','Harley','Zechariah','Gordon','Jakai','Carl','Graysen','Kylen','Ayan','Branson','Crosby','Dominik','Jabari','Jaxtyn','Kristopher','Ulises','Zyon','Fox','Howard','Salvatore','Turner','Vance','Harlem','Jair','Jakobe','Jeremias','Osiris','Azael','Bowie','Canaan','Elon','Granger','Karsyn','Zavier','Cain','Dangelo','Heath','Yisroel','Gian','Shepard','Harold','Kamdyn','Rene','Rodney','Yaakov','Adrien','Kartier','Cassian','Coleson','Ahmir','Darian','Genesis','Kalel','Agustin','Wylder','Yadiel','Ephraim','Kody','Neo','Ignacio','Osman','Aldo','Abdullah','Cory','Blaine','Dimitri','Khai','Landry','Palmer','Benedict','Leif','Koen','Maxton','Mordechai','Zev','Atharv','Bishop','Blaise','Davian' ]

lastNames=['Peterson','Hansley','Jenkins','Kora','Nora','Cromwel','Ashley','Bardot','Lopez','Hill','Tyson','Bolt','Sharpe','Cassidy','Langley','Monroe','West','Poverly','Raven','Daughtler','Madison','May','June','Solace','Hilton','Levine','Holly','Thatcher','McKenna','Marley','Ellis','Noel','Gonzales','Melenia','Hope','Cullen','Keller','Kade','Bandini','Elsher','Read','Collymore','McKay','Ford','Verlice','Stoll','Phoenix','Donovan','Huxley','Adler','Wisteria','Ledger','Hayes','Watson','Bryant','Alston','Harrison','Young','Samson','Zimmerman','Luna','Curran','Finnegan','Wilson','Dawson','Pierce','Adair','Davis','Underwood','Beckett','Gray','Kelly','Lincoln','Johnson','Blake','Gatlin','Howard','Martinez','Brooks','Miller','England','Finley','Knight','Bambi','Halifax','Aldaine','Amor','Amherst','Armstrong','Angeles','Crassus','Dalton','Danger','Annesley','Archer','Ash','Bancroft','Amanda','Creed','Delaney','Bradley','Crew','Freeze','Gramble','Raquel','Granger','Houston','Gryffon','Gunn','Alton','Delila','Whitfield','Ayton','Adair','Ashby','Auden','Baylor','Bingham','Banks','Bexley','Avery','Anderson','Allen','Adams','Carson','Carter','Valencia','Collins','Hendrix','Griffin','Rodgers','Nelsons','Trump','Hall','Cameron','Biden','Ramirez','Powell','Williams','Bryat','Lennon','Easton','Gasper','Wood','Philips','Channing','Dixon','Chamberlain','Emerson','Campbell','Bellamy','Remington','Wolverson','Nash','Parker','Walker','Sawyer','Coleman','Goodman','Jones','Jennings' ]

numbers=['1200', '0124', '0126', '0126', '0126', '0126', '0136', '0136', '0136', '0138', '0139', '0150', '0152', '0153', '0153', '0153', '0164', '0166', '0166', '0166', '0169', '0169', '0169', '0169', '0176', '0176', '0176', '0182', '0194', '0201', '0220', '0221', '0230', '0231', '0240', '0251', '0272', '0276', '0281', '0321', '0321', '0331', '0331', '0336', '0336', '0336', '0338', '0338', '0345', '0345', '0351', '0370', '0370', '0374', '0374', '0374', '0378', '0378', '0385', '0385', '0385', '0390', '0390', '0391', '0393', '0399', '0399', '0399', '0401', '0401', '0402', '0402', '0403', '0408', '0410', '0411', '0421', '0421', '0426', '0426', '0432', '0441', '0441', '0447', '0448', '0456', '0459', '0467', '0468', '0468', '0486', '0498', '0498', '0500', '0500', '0521', '0523', '0523', '0532', '0533', '0537', '0541', '0541', '0551', '0552', '0585', '0587', '0589', '0589', '0596', '0601', '0602', '0605', '0607', '0627', '0632', '0632', '0640', '0640', '0645', '0645', '0649', '0657', '0658', '0660', '0660', '0660', '0679', '0682', '0696', '0699', '0701', '0731', '0735', '0739', '0741', '0742', '0755', '0774', '0781', '0783', '0791', '0800', '0800', '0801', '0802', '0804', '0826', '0831', '0836', '0836', '0836', '0839', '0839', '0839', '0850', '0850', '0853', '0853', '0860', '0867', '0881', '0881', '0890', '0891', '0893', '0894', '0894', '0895', '0896', '0897', '0897', '0898', '0901', '0906', '0907', '0927', '0930', '0930', '0930', '0936', '0940', '0941', '0956', '0956', '0956', '0958', '0958', '0961', '0961', '0965', '0966', '0966', '0973', '0973', '0976', '0976', '0979', '0990', '0990', '0991', '0991', '0996', '1202', '1204', '1205', '1206', '1208', '1209', '1210', '1223', '1224', '1225', '1226', '1227', '1228', '1229', '1233', '1234', '1235', '1236', '1237', '1239', '1241', '1242', '1243', '1244', '1245', '1246', '1248', '1249', '1250', '1252', '1253', '1254', '1255', '1256', '1257', '1258', '1259', '1260', '1261', '1262', '1263', '1264', '1267', '1268', '1269', '1270', '1271', '1273', '1274', '1275', '1276', '1277', '1278', '1279', '1280', '1282', '1283', '1284', '1285', '1286', '1287', '1288', '1289', '1290', '1291', '1292', '1293', '1294', '1295', '1296', '1297', '1298', '1299', '1300', '1301', '1302', '1303', '1304', '1305', '1306', '1307', '1308', '1309', '1310', '1320', '1322', '1323', '1324', '1325', '1326', '1327', '1328', '1329', '1330', '1332', '1333', '1334', '1335', '1337', '1339', '1340', '1341', '1342', '1343', '1344', '1346', '1347', '1348', '1349', '1350', '1352', '1353', '1354', '1355', '1356', '1357', '1358', '1359', '1360', '1361', '1362', '1363', '1364', '1366', '1367', '1368', '1369', '1371', '1372', '1373', '1375', '1376', '1377', '1379', '1380', '1381', '1382', '1383', '1384', '1386', '1387', '1388', '1389', '1392', '1394', '1395', '1397', '1398', '1399', '1399', '1400', '1403', '1404', '1405', '1406', '1407', '1408', '1409', '1410', '1411', '1412', '1420', '1422', '1423', '1424', '1425', '1426', '1427', '1428', '1429', '1430', '1431', '1432', '1433', '1434', '1435', '1436', '1437', '1438', '1439', '1440', '1442', '1443', '1444', '1445', '1446', '1449', '1450', '1451', '1452', '1453', '1454', '1455', '1456', '1457', '1458', '1459', '1459', '1460', '1461', '1462', '1463', '1464', '1465', '1466', '1467', '1469', '1470', '1471', '1472', '1473', '1474', '1475', '1476', '1477', '1478', '1479', '1480', '1481', '1482', '1483', '1484', '1485', '1487', '1488', '1490', '1491', '1492', '1493', '1494', '1495', '1496', '1497', '1499', '1501', '1502', '1503', '1505', '1506', '1507', '1508', '1509', '1510', '1520', '1522', '1523', '1524', '1525', '1526', '1528', '1529', '1530', '1531', '1534', '1535', '1536', '1538', '1539', '1540', '1542', '1543', '1544', '1545', '1546', '1547', '1548', '1549', '1550', '1553', '1554', '1555', '1556', '1557', '1558', '1559', '1560', '1561', '1562', '1563', '1564', '1565', '1566', '1567', '1568', '1569', '1570', '1571', '1572', '1573', '1575', '1576', '1577', '1578', '1579', '1580', '1581', '1582', '1583', '1584', '1585', '1586', '1588', '1590', '1591', '1592', '1593', '1594', '1595', '1597', '1598', '1599', '1600', '1603', '1604', '1606', '1608', '1609', '1610', '1620', '1621', '1622', '1623', '1624', '1625', '1626', '1628', '1629', '1630', '1631', '1634', '1635', '1636', '1637', '1638', '1639', '1641', '1642', '1643', '1644', '1646', '1647', '1650', '1651', '1652', '1653', '1654', '1655', '1656', '1659', '1661', '1663', '1664', '1665', '1666', '1667', '1668', '1669', '1670', '1671', '1672', '1673', '1674', '1675', '1676', '1677', '1678', '1680', '1681', '1683', '1684', '1685', '1686', '1687', '1688', '1689', '1690', '1691', '1692', '1694', '1695', '1697', '1698', '1700', '1702', '1704', '1706', '1707', '1709', '1720', '1721', '1722', '1723', '1724', '1725', '1726', '1727', '1728', '1729', '1730', '1732', '1733', '1736', '1737', '1738', '1740', '1743', '1744', '1745', '1746', '1747', '1748', '1749', '1750', '1751', '1752', '1753', '1754', '1756', '1757', '1758', '1759', '1760', '1761', '1763', '1764', '1765', '1766', '1767', '1768', '1769', '1770', '1771', '1772', '1773', '1775', '1776', '1777', '1778', '1779', '1780', '1782', '1784', '1785', '1786', '1787', '1788', '1789', '1790', '1792', '1793', '1794', '1795', '1796', '1797', '1798', '1799', '1803', '1805', '1806', '1807', '1808', '1809', '1821', '1822', '1823', '1824', '1825', '1827', '1828', '1829', '1830', '1832', '1833', '1834', '1835', '1837', '1838', '1840', '1841', '1842', '1843', '1844', '1845', '1847', '1848', '1851', '1852', '1854', '1855', '1856', '1857', '1858', '1859', '1862', '1863', '1864', '1865', '1866', '1869', '1870', '1871', '1872', '1873', '1874', '1875', '1876', '1877', '1878', '1879', '1880', '1882', '1883', '1884', '1885', '1886', '1887', '1888', '1889', '1890', '1892', '1893', '1895', '1896', '1899', '1900', '1902', '1903', '1904', '1905', '1908', '1909', '1910', '1920', '1922', '1923', '1924', '1925', '1926', '1928', '1929', '1931', '1932', '1933', '1934', '1935', '1937', '1938', '1939', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1957', '1959', '1962', '1963', '1964', '1967', '1968', '1969', '1970', '1971', '1972', '1974', '1975', '1977', '1978', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1992', '1993', '1994', '1995', '1997', '4481', '4624', '7555', '0(1?)447', '01201 ', '01203 ', '01207 ', '01220 ', '01221 ', '01222 ', '01230 ', '01231 ', '01232 ', '01238 ', '01240 ', '01247 ', '01251 ', '01265 ', '01266 ', '01272 ', '01281 ', '01321 ', '01331 ', '01336 ', '01338 ', '01345 ', '01351 ', '01365 ', '01370 ', '01374 ', '01378 ', '01385 ', '01390 ', '01391 ', '01393 ', '01396 ', '01399 ', '01401 ', '01402 ', '01421 ', '01426 ', '01441 ', '01447 ', '01448 ', '01459 ', '01468 ', '01486 ', '01489 ', '01498 ', '01500 ', '01504 ', '01521 ', '01523 ', '01527 ', '01532 ', '01533 ', '01537 ', '01541 ', '01551 ', '01552 ', '01574 ', '01587 ', '01589 ', '01596 ', '01601 ', '01602 ', '01605 ', '01607 ', '01627 ', '01632 ', '01632 numbers', '01633 ', '01640 ', '01645 ', '01648 ', '01649 ', '01657 ', '01658 ', '01660 ', '01662 ', '01679 ', '01682 ', '01693 ', '01696 ', '01699 ', '01701 ', '01703 ', '01705 ', '01708 ', '01710–01719 ', '01731 ', '01734 ', '01735 ', '01739 ', '01741 ', '01742 ', '01755 ', '01762 ', '01774 ', '01781 ', '01783 ', '01791 ', '01800 ', '01801 ', '01802 ', '01804 ', '01810–01819 ', '01820 ', '01826 ', '01831 ', '01836 ', '01839 ', '01846 ', '01849 ', '01850 ', '01853 ', '01860 ', '01861 ', '01867 ', '01868 ', '01881 ', '01891 ', '01893 ', '01894 ', '01897 ', '01898 ', '01901 ', '01906 ', '01907 ', '01921 ', '01927 ', '01930 ', '01936 ', '01940 ', '01941 ', '01956 ', '01958 ', '01960 ', '01961 ', '01965 ', '01966 ', '01973 ', '01976 ', '01979 ', '01990 ', '01991 ', '01996 ', '01998 ', '01999 '  ]

gender = ['Male', 'Female']

possibleGrades = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'U']

emailSuffixes = ['gmail.com', 'yahoo.com', 'hotmail.com', 'hotmail.co.uk', 'yahoo.co.uk']

streetNames = ['High Street', 'Station Road', 'Main Street', 'Park Road', 'Church Road', 'Church Street', 'London Road', 'Victoria Road', 'Green Lane', 'Manor Road', 'Church Lane', 'Park Avenue', 'The Avenue', 'The Crescent', 'Queens Road', 'New Road', 'Grange Road', 'Kings Road', 'Kingsway', 'Windsor Road', 'Highfield Road', 'Mill Lane', 'Alexander Road', 'York Road', 'St. John’s Road', 'Main Road', 'Broadway', 'King Street', 'The Green', 'Springfield Road', 'George Street', 'Park Lane', 'Victoria Street', 'Albert Road', 'Queensway', 'New Street', 'Queen Street', 'West Street', 'North Street', 'Manchester Road', 'The Grove', 'Richmond Road', 'Grove Road', 'South Street', 'School Lane', 'The Drive', 'North Road', 'Stanley Road', 'Chester Road', 'Mill Road' ]

def randomPhoneNumbers():
    randomPrefix = random.randint(1, len(numbers))
    randomPrefix = numbers[randomPrefix - 1]
    randomPhoneNumber = random.randint(100000,999999)
    phoneNumber = randomPrefix + ',' + str(randomPhoneNumber)
    orgionalFile.at[eachRow, ['Phone Number']] = phoneNumber

def randomFirstNames():
    randomName = random.randint(1, len(firstNames))
    randomName = firstNames[randomName - 1]
    orgionalFile.at[eachRow, ['First Name']] = randomName

def randomSurNames():
    randomSurName = random.randint(1, len(lastNames))
    randomSurName = lastNames[randomSurName - 1]
    orgionalFile.at[eachRow, ['Last Name']] = randomSurName

def randomGender():
    randomGender = random.randint(1, len(gender))
    randomGender = gender[randomGender-1]
    orgionalFile.at[eachRow, ['Gender']] = randomGender

def randomGrade():
    randomGrade = random.randint(1, len(possibleGrades))
    randomGrade = possibleGrades[randomGrade -1]
    orgionalFile.at[eachRow, ['Grades']] = randomGrade

def randomEmail():
    randomEmail = random.randint(1, len(emailSuffixes))
    firstName = orgionalFile.iat[eachRow, 0]
    surName = orgionalFile.iat[eachRow, 1]
    randomEmail = firstName + "." + surName + str(random.randint(1, 999)) + "@" + emailSuffixes[randomEmail - 1]
    orgionalFile.at[eachRow, ['Email']] = randomEmail

def checkLuhn(cardNo):
    
    nDigits = len(cardNo)
    nSum = 0
    isSecond = False
     
    for i in range(nDigits - 1, -1, -1):
        d = ord(cardNo[i]) - ord('0')
     
        if (isSecond == True):
            d = d * 2
  
        # We add two digits to handle ccases that make two digits after doubling
        nSum += d // 10
        nSum += d % 10
  
        isSecond = not isSecond
     
    if (nSum % 10 == 0):
        return True
    else:
        return False

def creditCardNumber():
    cardNumberCheck = str(random.randint(1000000000000000,9999999999999999))
    while checkLuhn(cardNumberCheck) == False:
        cardNumberCheck = str(random.randint(1000000000000000,9999999999999999))
        checkLuhn(cardNumberCheck)
    orgionalFile.at[eachRow, ['Credit Card Numbers']] = cardNumberCheck

def randomPostCode():
    numberOfLetters = random.randint(1,2)
    if numberOfLetters == 1:
        letterNumber = random.randint(1, len(alphabetList))
        startPostCode = alphabetList[letterNumber - 1]
    elif numberOfLetters == 2:
        letterNumber1 = random.randint(1, len(alphabetList))
        firstLetter = alphabetList[letterNumber1 - 1]
        letterNumber2 = random.randint(1, len(alphabetList))
        secondLetter = alphabetList[letterNumber2 - 1]
        startPostCode = firstLetter + secondLetter
    
    postCode = startPostCode + str(random.randint(1, 9)) + str(random.randint(1, 9)) + " " + alphabetList[random.randint(1, (len(alphabetList)-1))] + str(random.randint(1, 9)) + str(random.randint(1, 9)) 
    orgionalFile.at[eachRow, ['Post Codes']] = postCode

def randomStreetName():
    streetName = str(random.randint(1, 250)) + " " + streetNames[random.randint(1, (len(streetNames)-1))]
    orgionalFile.at[eachRow, ['Street Names']] = streetName
    pass         

#empty the origional file
# for eachRow in range(0, rowNumbers):
#     columnCount = len(orgionalFile.columns)
#     for eachColumn in range(0, columnCount):
#         orgionalFile.iat[eachRow, eachColumn] = 'NaN'
#         orgionalFile.to_csv("/Users/hunteradder626/Documents/Csv/Fake Data.csv", index=False)

for eachRow in range(0,10):
    randomFirstNames()
    randomSurNames()
    randomPhoneNumbers()
    randomGender()
    randomGrade( )
    randomEmail()
    creditCardNumber()
    randomPostCode()
    randomStreetName()

print (orgionalFile)

orgionalFile.to_csv("/Users/hunteradder626/Documents/Csv/Fake Data.csv", index=False)