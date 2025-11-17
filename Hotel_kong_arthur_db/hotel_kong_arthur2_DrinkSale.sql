-- MySQL dump 10.13  Distrib 8.0.44, for macos15 (arm64)
--
-- Host: localhost    Database: hotel_kong_arthur2
-- ------------------------------------------------------
-- Server version	9.5.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

--
-- Table structure for table `DrinkSale`
--

DROP TABLE IF EXISTS `DrinkSale`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DrinkSale` (
  `sale_id` int NOT NULL AUTO_INCREMENT,
  `drink_name` varchar(50) DEFAULT NULL,
  `category` varchar(50) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `units_sold` int DEFAULT NULL,
  `total_sale` int DEFAULT NULL,
  PRIMARY KEY (`sale_id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DrinkSale`
--

LOCK TABLES `DrinkSale` WRITE;
/*!40000 ALTER TABLE `DrinkSale` DISABLE KEYS */;
INSERT INTO `DrinkSale` VALUES (1,'Margarita','Cocktail',72,2361,171102),(2,'Mojito','Cocktail',142,3350,476973),(3,'Old Fashioned','Cocktail',129,3154,407402),(4,'Martini','Cocktail',132,3754,496166),(5,'Daiquiri','Cocktail',102,3469,355364),(6,'Negroni','Cocktail',149,2691,402251),(7,'Whiskey Sour','Cocktail',96,3824,366072),(8,'Cosmopolitan','Cocktail',91,2594,237092),(9,'Mai Tai','Cocktail',76,2279,174116),(10,'Pina Colada','Cocktail',111,3699,410811),(11,'Bloody Mary','Cocktail',127,3632,461990),(12,'Gin and Tonic','Cocktail',127,3602,457670),(13,'Sidecar','Cocktail',104,2457,255430),(14,'Manhattan','Cocktail',87,2413,208990),(15,'Espresso Martini','Cocktail',86,3763,324182),(16,'French 75','Cocktail',134,3168,425494),(17,'Caipirinha','Cocktail',106,2802,298217),(18,'Mint Julep','Cocktail',144,3653,524352),(19,'Tom Collins','Cocktail',104,3344,348679),(20,'Long Island Iced Tea','Cocktail',146,2068,302404),(21,'Espresso','Coffee',69,14656,1012730),(22,'Americano','Coffee',41,13833,564940),(23,'Latte','Coffee',63,11355,717522),(24,'Cappuccino','Coffee',51,11676,593958),(25,'Macchiato','Coffee',61,10389,637988),(26,'Mocha','Coffee',61,13897,842019),(27,'Flat White','Coffee',33,10249,342624),(28,'Cortado','Coffee',54,10354,564293),(29,'Iced Coffee','Coffee',35,10337,359624),(30,'Affogato','Coffee',64,11135,708186);
/*!40000 ALTER TABLE `DrinkSale` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-11-05  0:19:16
