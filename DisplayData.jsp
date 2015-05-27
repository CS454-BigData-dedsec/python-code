<?xml version="1.0" encoding="ISO-8859-1" ?>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<jsp:useBean id="cl" class="model.ChampionListBean" scope="page"/>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions" %>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
<head>
<style>
body {
    width: 600px;
    margin: 40px auto;
    font-family: 'trebuchet MS', 'Lucida sans', Arial;
    font-size: 14px;
    color: #444;
}

table {
    *border-collapse: collapse; /* IE7 and lower */
    border-spacing: 0;
    width: 100%;    
}

.bordered {
    border: solid #ccc 1px;
    -moz-border-radius: 6px;
    -webkit-border-radius: 6px;
    border-radius: 6px;
    -webkit-box-shadow: 0 1px 1px #ccc; 
    -moz-box-shadow: 0 1px 1px #ccc; 
    box-shadow: 0 1px 1px #ccc;         
}

.bordered tr {
    background: #fbf8e9;
    -o-transition: all 0.1s ease-in-out;
    -webkit-transition: all 0.1s ease-in-out;
    -moz-transition: all 0.1s ease-in-out;
    -ms-transition: all 0.1s ease-in-out;
    transition: all 0.1s ease-in-out;     
}    
    
.bordered td, .bordered th {
    border-left: 1px solid #ccc;
    border-top: 1px solid #ccc;
    padding: 10px;
    text-align: center;    
}

.bordered th {
    background-color: #dce9f9;
    background-image: -webkit-gradient(linear, left top, left bottom, from(#ebf3fc), to(#dce9f9));
    background-image: -webkit-linear-gradient(top, #ebf3fc, #dce9f9);
    background-image:    -moz-linear-gradient(top, #ebf3fc, #dce9f9);
    background-image:     -ms-linear-gradient(top, #ebf3fc, #dce9f9);
    background-image:      -o-linear-gradient(top, #ebf3fc, #dce9f9);
    background-image:         linear-gradient(top, #ebf3fc, #dce9f9);
    -webkit-box-shadow: 0 1px 0 rgba(255,255,255,.8) inset; 
    -moz-box-shadow:0 1px 0 rgba(255,255,255,.8) inset;  
    box-shadow: 0 1px 0 rgba(255,255,255,.8) inset;        
    border-top: none;
    text-shadow: 0 1px 0 rgba(255,255,255,.5); 
}

.bordered td:first-child, .bordered th:first-child {
    border-left: none;
}

.bordered th:first-child {
    -moz-border-radius: 6px 0 0 0;
    -webkit-border-radius: 6px 0 0 0;
    border-radius: 6px 0 0 0;
}

.bordered th:last-child {
    -moz-border-radius: 0 6px 0 0;
    -webkit-border-radius: 0 6px 0 0;
    border-radius: 0 6px 0 0;
}

.bordered th:only-child{
    -moz-border-radius: 6px 6px 0 0;
    -webkit-border-radius: 6px 6px 0 0;
    border-radius: 6px 6px 0 0;
}

.bordered tr:last-child td:first-child {
    -moz-border-radius: 0 0 0 6px;
    -webkit-border-radius: 0 0 0 6px;
    border-radius: 0 0 0 6px;
}

.bordered tr:last-child td:last-child {
    -moz-border-radius: 0 0 6px 0;
    -webkit-border-radius: 0 0 6px 0;
    border-radius: 0 0 6px 0;
}

.bordered tbody tr:nth-child(even) {
    background: #ccc;
    -webkit-box-shadow: 0 1px 0 rgba(255,255,255,.8) inset; 
    -moz-box-shadow:0 1px 0 rgba(255,255,255,.8) inset;  
    box-shadow: 0 1px 0 rgba(255,255,255,.8) inset;        
}
/* I added this code below here to make the rows solid color*/
.borered tbody tr:nth-child(odd) {
    background: #ccc;
    -webkit-box-shadow: 0 1px 0 rgba(255,255,255,.8) inset; 
    -moz-box-shadow:0 1px 0 rgba(255,255,255,.8) inset;  
    box-shadow: 0 1px 0 rgba(255,255,255,.8) inset;        
}
/* CODE FOR THE MENUE BELOW */
#dolphincontainer { 
	position:relative;
	height:40px; /* HEIGHT OF THE BLUE BAR BELOW THE MENU */
	color:#E0E0E0;
	background:#143D55;
	width:100%;
	font-family:Helvetica,Arial,Verdana,sans-serif;
}

#dolphinnav {
	position:relative;
	height:33px;
	font-size:12px;
	text-transform:uppercase;
	font-weight:bold;
	background:#fff url(dolphin_bg.gif) repeat-x bottom left;
	padding:0 0 0 20px;
}

#dolphinnav ul {
	margin:0;
	padding:0;
	list-style-type:none;
	width:auto;
	float:left;
}

#dolphinnav ul li {
	display:block;
	float:left;
	margin:0 1px;
}

#dolphinnav ul li a {
	display:block;
	float:left;
	color:#EAF3F8;
	text-decoration:none;
	padding:0 0 0 33px;
	height:33px;
}

#dolphinnav ul li a span {
	padding:12px 20px 0 0;
	height:21px;
	float:left;
}

#dolphinnav ul li a:hover {
	color:#fff;
	background:transparent url(dolphin_bg-OVER.gif) repeat-x bottom left;
}

#dolphinnav ul li a:hover span {
	display:block;
	width:auto;
	cursor:pointer;
}

#dolphinnav ul li a.current,#dolphinnav ul li a.current:hover {
	color:#fff;
	background:#1D6893 url(dolphin_left-ON.gif) no-repeat top left;
	line-height:275%;
	
}

#dolphinnav ul li a.current span {
	display:block;
	padding:5 20px 5 5;
	width:auto;
	background:#1D6893 url(dolphin_right-ON.gif) no-repeat top right;
	height:33px;
}

  
</style>
<div style='position:ablsolute;z-index:0;left:0;top:0;width:100%;height:100%'>
         <img src='logo.png' style='width:100%;height:100%'  />
</div>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>Champion Data</title>
</head>
<body background="background.jpg" bgproperties="fixed">
<div id="dolphincontainer">
<div id="dolphinnav">
<form action="http://localhost:8080/leagueoflegends/PullData" method="get" >
 <ul>
  <li><a href="" title=""><span>Home</span></a></li>
  <li><a href="" title="" ><span>About Us</span></a></li>
  <li><a href="http://localhost:8080/leagueoflegends/DisplayData.jsp"><span>Champion Data</span></a></li>
  <li><span><input type="text"  name="champ"/></span></li>
  <li><span><input type="submit" value="search"/></span></li>
 </ul>
 </form>
</div>
</div>
<c:if test="${fn:length(cl.champList) == 0 }" >
There are no Champions in the list!!!
</c:if>

<c:if test="${fn:length(cl.champList) > 0 }" > 
<table class="bordered">
<tr>
	<td><h4>Image</h4></td>
	<td><h4>Name</h4></td>
	<td><h4>Games Played</h4></td>
	<td><h4>Wins</h4></td>
	<td><h4>Loses</h4></td>
	<td><h4>Win Ratio</h4></td>
	<td><h4>Loss Ratio</h4></td>
</tr>

<c:forEach items="${cl.champList}" var="champs">
<tr>
	<td><a href=""><img src="${champs.image}"></img></a></td>
	<td><a href="">${champs.name}</a></td>
	<td>${champs.numberOfGames }</td>
	<td>${champs.wins}</td>
	<td>${champs.loses}</td>
	<td><fmt:formatNumber type="number" maxFractionDigits="3" value="${champs.winRatio}"/></td>
	<td><fmt:formatNumber type="number" maxFractionDigits="3" value="${champs.lossRatio}"/></td>
</tr>
</c:forEach>
</table>


</c:if>

</body>
</html>
