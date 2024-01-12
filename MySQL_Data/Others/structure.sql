CREATE DATABASE  IF NOT EXISTS `final_final` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `final_final`;
-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: final_final
-- ------------------------------------------------------
-- Server version	8.0.31

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

--
-- Table structure for table `cart`
--

DROP TABLE IF EXISTS `cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cart` (
  `cart_id` int NOT NULL,
  `amount` int DEFAULT NULL,
  PRIMARY KEY (`cart_id`),
  UNIQUE KEY `index_cart` (`cart_id`),
  KEY `index_cart_amt` (`amount`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `clothing`
--

DROP TABLE IF EXISTS `clothing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clothing` (
  `p_id` int NOT NULL,
  `category` varchar(255) NOT NULL,
  `size` int NOT NULL,
  `type_of_clothing` varchar(255) NOT NULL,
  PRIMARY KEY (`p_id`),
  CONSTRAINT `clothing_ibfk_1` FOREIGN KEY (`p_id`) REFERENCES `product` (`p_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `consumables`
--

DROP TABLE IF EXISTS `consumables`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `consumables` (
  `p_id` int NOT NULL,
  `date_of_expiry` date NOT NULL,
  `ingredients` varchar(255) NOT NULL,
  PRIMARY KEY (`p_id`),
  CONSTRAINT `consumables_ibfk_1` FOREIGN KEY (`p_id`) REFERENCES `product` (`p_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `contains_table`
--

DROP TABLE IF EXISTS `contains_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contains_table` (
  `qty` int DEFAULT NULL,
  `cart_id` int NOT NULL,
  `p_id` int NOT NULL,
  PRIMARY KEY (`cart_id`,`p_id`),
  UNIQUE KEY `index_contains` (`cart_id`,`p_id`),
  KEY `p_id` (`p_id`),
  KEY `index_contains_qty` (`qty`),
  CONSTRAINT `contains_table_ibfk_1` FOREIGN KEY (`cart_id`) REFERENCES `cart` (`cart_id`),
  CONSTRAINT `contains_table_ibfk_2` FOREIGN KEY (`p_id`) REFERENCES `product` (`p_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `cosmetics`
--

DROP TABLE IF EXISTS `cosmetics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cosmetics` (
  `p_id` int NOT NULL,
  `date_of_expiry` date NOT NULL,
  `composition` varchar(255) NOT NULL,
  `directions_of_use` varchar(255) NOT NULL,
  PRIMARY KEY (`p_id`),
  CONSTRAINT `cosmetics_ibfk_1` FOREIGN KEY (`p_id`) REFERENCES `product` (`p_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `cust_contact`
--

DROP TABLE IF EXISTS `cust_contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cust_contact` (
  `c_id` int NOT NULL,
  `cust_contact` varchar(20) NOT NULL,
  PRIMARY KEY (`c_id`,`cust_contact`),
  CONSTRAINT `cust_contact_ibfk_1` FOREIGN KEY (`c_id`) REFERENCES `customer` (`c_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `c_id` int NOT NULL,
  `cust_first_name` varchar(255) DEFAULT NULL,
  `cust_last_name` varchar(255) DEFAULT NULL,
  `cust_dob` date DEFAULT NULL,
  `cust_street` varchar(255) DEFAULT NULL,
  `cust_city` varchar(255) DEFAULT NULL,
  `cust_state` varchar(255) DEFAULT NULL,
  `cust_pin` varchar(255) DEFAULT NULL,
  `cust_age` int DEFAULT NULL,
  `cust_title` varchar(255) DEFAULT NULL,
  `cust_type` varchar(20) NOT NULL DEFAULT 'regular',
  PRIMARY KEY (`c_id`),
  UNIQUE KEY `index_customer` (`c_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `Customer_age_trigger` BEFORE INSERT ON `customer` FOR EACH ROW set
new.cust_age = 2023 - year(new.cust_dob) */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `delivers`
--

DROP TABLE IF EXISTS `delivers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `delivers` (
  `e_id` int NOT NULL,
  `order_id` int NOT NULL,
  `tracking_status` varchar(255) DEFAULT NULL,
  `w_id` int DEFAULT NULL,
  PRIMARY KEY (`e_id`,`order_id`),
  UNIQUE KEY `index_delivers` (`order_id`),
  KEY `w_id` (`w_id`),
  KEY `index_delivers_track` (`tracking_status`),
  CONSTRAINT `delivers_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `order_table` (`order_id`),
  CONSTRAINT `delivers_ibfk_2` FOREIGN KEY (`w_id`) REFERENCES `warehouse` (`w_id`),
  CONSTRAINT `delivers_ibfk_3` FOREIGN KEY (`e_id`) REFERENCES `employee` (`e_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `electronics`
--

DROP TABLE IF EXISTS `electronics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `electronics` (
  `p_id` int NOT NULL,
  `voltage` int NOT NULL,
  `warranty` int NOT NULL,
  PRIMARY KEY (`p_id`),
  CONSTRAINT `electronics_ibfk_1` FOREIGN KEY (`p_id`) REFERENCES `product` (`p_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `emp_contact`
--

DROP TABLE IF EXISTS `emp_contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `emp_contact` (
  `emp_contact` varchar(20) NOT NULL,
  `e_id` int NOT NULL,
  PRIMARY KEY (`e_id`,`emp_contact`),
  UNIQUE KEY `index_emp_cont` (`e_id`,`emp_contact`),
  CONSTRAINT `emp_contact_ibfk_1` FOREIGN KEY (`e_id`) REFERENCES `employee` (`e_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `e_id` int NOT NULL,
  `emp_name` varchar(255) DEFAULT NULL,
  `base_salary` int NOT NULL DEFAULT ((case `emp_type` when _utf8mb4'junior' then 25000 when _utf8mb4'senior' then 80000 end)),
  `emp_street` varchar(255) DEFAULT NULL,
  `emp_state` varchar(255) DEFAULT NULL,
  `emp_city` varchar(255) DEFAULT NULL,
  `emp_pin` varchar(255) DEFAULT NULL,
  `emp_role` varchar(255) DEFAULT NULL,
  `emp_type` varchar(255) DEFAULT NULL,
  `increment` int DEFAULT NULL,
  `emp_dob` date DEFAULT NULL,
  `emp_age` int DEFAULT NULL,
  PRIMARY KEY (`e_id`),
  UNIQUE KEY `index_employee` (`e_id`),
  KEY `index_emp_role` (`emp_role`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `Employee_age_update` BEFORE INSERT ON `employee` FOR EACH ROW set
new.emp_age = (2022 - new.emp_dob) */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `increment`
--

DROP TABLE IF EXISTS `increment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `increment` (
  `w_id` int NOT NULL,
  `e_id` int NOT NULL,
  `date_of_increment` date NOT NULL,
  `amount` int DEFAULT NULL,
  PRIMARY KEY (`w_id`,`e_id`,`date_of_increment`),
  UNIQUE KEY `index_incre` (`w_id`,`e_id`,`date_of_increment`),
  KEY `e_id` (`e_id`),
  KEY `index_increment` (`amount`),
  CONSTRAINT `increment_ibfk_1` FOREIGN KEY (`w_id`) REFERENCES `warehouse` (`w_id`),
  CONSTRAINT `increment_ibfk_2` FOREIGN KEY (`e_id`) REFERENCES `employee` (`e_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `manager`
--

DROP TABLE IF EXISTS `manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manager` (
  `date_of_promotion` date DEFAULT NULL,
  `e_id` int NOT NULL,
  PRIMARY KEY (`e_id`),
  UNIQUE KEY `index_manager` (`e_id`),
  CONSTRAINT `manager_ibfk_1` FOREIGN KEY (`e_id`) REFERENCES `employee` (`e_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `order_table`
--

DROP TABLE IF EXISTS `order_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_table` (
  `order_id` int NOT NULL,
  `discount` int DEFAULT NULL,
  `date_of_order` date DEFAULT NULL,
  `c_id` int DEFAULT NULL,
  `cart_id` int DEFAULT NULL,
  `type_of_payment` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`order_id`),
  UNIQUE KEY `index_order` (`order_id`),
  KEY `c_id` (`c_id`),
  KEY `cart_id` (`cart_id`),
  KEY `index_discount` (`discount`),
  CONSTRAINT `order_table_ibfk_1` FOREIGN KEY (`c_id`) REFERENCES `customer` (`c_id`),
  CONSTRAINT `order_table_ibfk_2` FOREIGN KEY (`cart_id`) REFERENCES `cart` (`cart_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `Discount` BEFORE INSERT ON `order_table` FOR EACH ROW BEGIN
IF (select cust_type from Customer where c_id = new.c_id) =
'premium' THEN
SET new.Discount := 20;
ELSEIF (select cust_type from Customer where c_id =
new.c_id) = 'imperia' THEN
SET new.Discount = 25;
ELSE
SET new.Discount = 10;
END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `performance`
--

DROP TABLE IF EXISTS `performance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `performance` (
  `e_id` int NOT NULL,
  `performance_this_qtr` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`e_id`),
  CONSTRAINT `performance_ibfk_1` FOREIGN KEY (`e_id`) REFERENCES `employee` (`e_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `p_id` int NOT NULL,
  `date_of_mfg` varchar(255) DEFAULT NULL,
  `prod_name` varchar(255) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `qty` int DEFAULT NULL,
  `net_weight` int NOT NULL,
  `manufacturing_company` varchar(255) DEFAULT NULL,
  `prod_type` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `index_product` (`p_id`),
  KEY `index_product_name` (`prod_name`),
  KEY `index_product_type` (`prod_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `review`
--

DROP TABLE IF EXISTS `review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `review` (
  `order_id` int NOT NULL,
  `review_text` varchar(255) DEFAULT NULL,
  `date_and_time_of_review` datetime NOT NULL,
  `type_of_review` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`order_id`,`date_and_time_of_review`),
  CONSTRAINT `review_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `order_table` (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `supplies`
--

DROP TABLE IF EXISTS `supplies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supplies` (
  `supply_id` int NOT NULL,
  `v_id` int DEFAULT NULL,
  `w_id` int DEFAULT NULL,
  `p_id` int DEFAULT NULL,
  `date_of_supply` date DEFAULT NULL,
  `qty_supplied` bigint DEFAULT NULL,
  `total_amount` double DEFAULT NULL,
  PRIMARY KEY (`supply_id`),
  KEY `w_id` (`w_id`),
  KEY `p_id` (`p_id`),
  KEY `v_id` (`v_id`),
  CONSTRAINT `supplies_ibfk_1` FOREIGN KEY (`w_id`) REFERENCES `warehouse` (`w_id`),
  CONSTRAINT `supplies_ibfk_2` FOREIGN KEY (`p_id`) REFERENCES `product` (`p_id`),
  CONSTRAINT `supplies_ibfk_3` FOREIGN KEY (`v_id`) REFERENCES `vendor` (`v_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `updates`
--

DROP TABLE IF EXISTS `updates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `updates` (
  `update_id` int NOT NULL,
  `cart_id` int DEFAULT NULL,
  `c_id` int DEFAULT NULL,
  `type_of_updation` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`update_id`),
  UNIQUE KEY `index_updates` (`update_id`),
  KEY `cart_id` (`cart_id`),
  KEY `c_id` (`c_id`),
  KEY `index_update_type` (`type_of_updation`),
  CONSTRAINT `updates_ibfk_1` FOREIGN KEY (`cart_id`) REFERENCES `cart` (`cart_id`),
  CONSTRAINT `updates_ibfk_2` FOREIGN KEY (`c_id`) REFERENCES `customer` (`c_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `vendor`
--

DROP TABLE IF EXISTS `vendor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vendor` (
  `vendor_name` varchar(255) DEFAULT NULL,
  `v_id` int NOT NULL,
  `vendor_city` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`v_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `vendor_contact`
--

DROP TABLE IF EXISTS `vendor_contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vendor_contact` (
  `vendor_contact` varchar(20) NOT NULL,
  `v_id` int NOT NULL,
  PRIMARY KEY (`v_id`,`vendor_contact`),
  CONSTRAINT `vendor_contact_ibfk_1` FOREIGN KEY (`v_id`) REFERENCES `vendor` (`v_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ware_contact`
--

DROP TABLE IF EXISTS `ware_contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ware_contact` (
  `w_id` int NOT NULL,
  `ware_contact` varchar(20) NOT NULL,
  PRIMARY KEY (`w_id`,`ware_contact`),
  CONSTRAINT `ware_contact_ibfk_1` FOREIGN KEY (`w_id`) REFERENCES `warehouse` (`w_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `warehouse`
--

DROP TABLE IF EXISTS `warehouse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `warehouse` (
  `w_id` int NOT NULL,
  `ware_street` varchar(255) DEFAULT NULL,
  `ware_city` varchar(255) DEFAULT NULL,
  `ware_state` varchar(255) DEFAULT NULL,
  `ware_pin` varchar(255) DEFAULT NULL,
  `ware_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`w_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `works_for`
--

DROP TABLE IF EXISTS `works_for`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `works_for` (
  `date_of_appointment` date NOT NULL,
  `e_id` int NOT NULL,
  `w_id` int NOT NULL,
  PRIMARY KEY (`e_id`,`w_id`,`date_of_appointment`),
  UNIQUE KEY `index_works_for` (`e_id`,`w_id`,`date_of_appointment`),
  KEY `w_id` (`w_id`),
  CONSTRAINT `works_for_ibfk_1` FOREIGN KEY (`e_id`) REFERENCES `employee` (`e_id`),
  CONSTRAINT `works_for_ibfk_2` FOREIGN KEY (`w_id`) REFERENCES `warehouse` (`w_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping events for database 'final_final'
--

--
-- Dumping routines for database 'final_final'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-19 20:47:28
