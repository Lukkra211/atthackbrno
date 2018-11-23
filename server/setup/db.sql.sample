-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 16, 2018 at 11:15 PM
-- Server version: 10.1.28-MariaDB
-- PHP Version: 7.1.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `quiz`
--

-- --------------------------------------------------------

--
-- Table structure for table `answers`
--

CREATE TABLE `answers` (
  `ID` int(11) NOT NULL,
  `name` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `startTime` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `AQ1` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `timeAQ1` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `AQ2` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `timeAQ2` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `AQ3` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `timeAQ3` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `AQ4` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `timeAQ4` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `AQ5` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `timeAQ5` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `AQ6` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `timeAQ6` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `AQ7` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `timeAQ7` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `AQ8` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `timeAQ8` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `AQ9` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `timeAQ9` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `AQ10` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `timeAQ10` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `AQ11` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `timeAQ11` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `AQ12` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `timeAQ12` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `AQ13` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `timeAQ13` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `AQ14` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `timeAQ14` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `AQ15` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `timeAQ15` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `AQ16` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `timeAQ16` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `AQ17` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `timeAQ17` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `AQ18` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `timeAQ18` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `AQ19` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `timeAQ19` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `AQ20` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `timeAQ20` varchar(45) COLLATE utf8_czech_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_czech_ci;

-- --------------------------------------------------------

--
-- Table structure for table `question`
--

CREATE TABLE `question` (
  `id_question` int(11) NOT NULL,
  `wording` varchar(250) COLLATE utf8_czech_ci NOT NULL,
  `correct` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `answer1` varchar(250) COLLATE utf8_czech_ci NOT NULL,
  `answer2` varchar(250) COLLATE utf8_czech_ci NOT NULL,
  `answer3` varchar(250) COLLATE utf8_czech_ci NOT NULL,
  `answer4` varchar(250) COLLATE utf8_czech_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_czech_ci;

-- --------------------------------------------------------

--
-- Table structure for table `questionset`
--

CREATE TABLE `questionset` (
  `id_qs` int(11) NOT NULL,
  `name` varchar(250) COLLATE utf8_czech_ci NOT NULL,
  `questions` varchar(250) COLLATE utf8_czech_ci NOT NULL,
  `admins` int(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_czech_ci;

-- --------------------------------------------------------

--
-- Table structure for table `rank`
--

CREATE TABLE `rank` (
  `ID` int(11) NOT NULL,
  `user_name` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `saveTime` bigint(45) NOT NULL,
  `score` int(11) NOT NULL,
  `solutionTime` varchar(45) COLLATE utf8_czech_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_czech_ci;

-- --------------------------------------------------------

--
-- Table structure for table `settings`
--

CREATE TABLE `settings` (
  `id` int(11) NOT NULL,
  `name` varchar(45) COLLATE utf8_czech_ci NOT NULL,
  `countOfActiveQuestions` int(11) NOT NULL,
  `idOfActiveQuestionSet` int(11) NOT NULL,
  `autoSave` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_czech_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id_user` int(11) NOT NULL,
  `username` varchar(250) COLLATE utf8_czech_ci NOT NULL,
  `password` varchar(250) COLLATE utf8_czech_ci NOT NULL,
  `nick` varchar(250) COLLATE utf8_czech_ci NOT NULL,
  `email` varchar(250) COLLATE utf8_czech_ci NOT NULL,
  `afterLogonGoTo` varchar(45) COLLATE utf8_czech_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_czech_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id_user`, `username`, `password`, `nick`, `email`, `afterLogonGoTo`) VALUES
(1, 'admin', 'admin', 'Administrator', 'mail@example.com', 'dashboard.php');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `answers`
--
ALTER TABLE `answers`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `question`
--
ALTER TABLE `question`
  ADD PRIMARY KEY (`id_question`);

--
-- Indexes for table `questionset`
--
ALTER TABLE `questionset`
  ADD PRIMARY KEY (`id_qs`);

--
-- Indexes for table `rank`
--
ALTER TABLE `rank`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `settings`
--
ALTER TABLE `settings`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id_user`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `answers`
--
ALTER TABLE `answers`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20793;

--
-- AUTO_INCREMENT for table `question`
--
ALTER TABLE `question`
  MODIFY `id_question` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `questionset`
--
ALTER TABLE `questionset`
  MODIFY `id_qs` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `rank`
--
ALTER TABLE `rank`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20621;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
