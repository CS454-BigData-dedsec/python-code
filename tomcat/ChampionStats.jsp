<?xml version="1.0" encoding="ISO-8859-1" ?>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<jsp:useBean id="toplossitems" class="model.ItemsBean" scope="session"/>
<jsp:useBean id="topwinitems" class="model.ItemsBean" scope="session"/>

<jsp:useBean id="winningrolelist" class="model.RoleBean" scope="session"/>
<jsp:useBean id="losingrolelist" class="model.RoleBean" scope="session"/>

<jsp:useBean id="toplossingspells" class="model.SpellBean" scope="session"/>
<jsp:useBean id="topwinningspells" class="model.SpellBean" scope="session"/>

<jsp:useBean id="winninglanelist" class="model.LaneBean" scope="session"/>
<jsp:useBean id="losinglanelist" class="model.LaneBean" scope="session"/>
<jsp:useBean id="champ" class="model.Champion" scope="session"/>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions" %>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %><html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
        <script type="text/javascript">
      google.load("visualization", "1", {packages:["corechart"]});
google.setOnLoadCallback(drawVisualization);

function drawVisualization() {
  // Some raw data (not necessarily accurate)
  var data = google.visualization.arrayToDataTable([
    ['Month', ''],
<c:forEach items="${topwinningspells.spellList}" var="lane" >
<c:set var="message" value="${lane.name}"/>
    ['<c:out value="${message}"/>',${lane.count}],    
</c:forEach>
    ['', 0]
  ]);

  var options = {
    title : 'Spells most commonly used by the winners',
    vAxis: {title: "times spell selected for a match"},
    hAxis: {title: "Spells "},
    seriesType: "bars",
    series: {5: {type: "line"}}
  };

  var chart = new google.visualization.ComboChart(document.getElementById('SpellW_div'));
  chart.draw(data, options);
}
    </script>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["corechart"]});
google.setOnLoadCallback(drawVisualization);

function drawVisualization() {
  // Some raw data (not necessarily accurate)
  var data = google.visualization.arrayToDataTable([
    ['Month', ''],
<c:forEach items="${toplossingspells.spellList}" var="lane" >
<c:set var="message" value="${lane.name}"/>
    ['<c:out value="${message}"/>',${lane.count}],    
</c:forEach>
    ['', 0]
  ]);
  var options = {
    title : 'Spells most commonly used by the lossers',
    vAxis: {title: "times spell selected for a match"},
    hAxis: {title: "Spells "},
    seriesType: "bars",
    series: {5: {type: "line"}}
  };

  var chart = new google.visualization.ComboChart(document.getElementById('SpellL_div'));
  chart.draw(data, options);
}
    </script>
            <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["corechart"]});
google.setOnLoadCallback(drawVisualization);

function drawVisualization() {
  // Some raw data (not necessarily accurate)
  var data = google.visualization.arrayToDataTable([
    ['Month', ''],
<c:forEach items="${topwinitems.itemList}" var="lane" >
<c:set var="message" value="${lane.name}"/>
    ['<c:out value="${message}"/>',${lane.count}],    
</c:forEach>
    ['', 0]
  ]);

  var options = {
    title : 'Items most commonly used by the winners',
    vAxis: {title: "times item was used for this champion"},
    hAxis: {title: "Items "},
    seriesType: "bars",
    series: {5: {type: "line"}}
  };

  var chart = new google.visualization.ComboChart(document.getElementById('ItemsW_div'));
  chart.draw(data, options);
}
    </script>
        <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["corechart"]});
google.setOnLoadCallback(drawVisualization);

function drawVisualization() {
  // Some raw data (not necessarily accurate)
  var data = google.visualization.arrayToDataTable([
    ['Month', ''],
<c:forEach items="${toplossitems.itemList}" var="lane" >
<c:set var="message" value="${lane.name}"/>
    ['<c:out value="${message}"/>',${lane.count}],    
</c:forEach>
    ['',  0]
  ]);

  var options = {
    title : 'Items most commonly used by the lossers',
    vAxis: {title: "times item was used for this champion"},
    hAxis: {title: "Items "},
    seriesType: "bars",
    series: {5: {type: "line"}}
  };

  var chart = new google.visualization.ComboChart(document.getElementById('ItemsL_div'));
  chart.draw(data, options);
}
    </script>
            <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["corechart"]});
google.setOnLoadCallback(drawVisualization);

function drawVisualization() {
  // Some raw data (not necessarily accurate)
  var data = google.visualization.arrayToDataTable([
    ['Month', ''],
<c:forEach items="${winninglanelist.laneList}" var="lane" >
<c:set var="message" value="${lane.name}"/>
    ['<c:out value="${message}"/>',${lane.count}],    
</c:forEach>
    ['', 0]
  ]);

  var options = {
    title : 'Lanes most commonly used by winning players',
    vAxis: {title: "# of times  "},
    hAxis: {title: "Lanes "},
    seriesType: "bars",
    series: {5: {type: "line"}}
  };

  var chart = new google.visualization.ComboChart(document.getElementById('LanesW_div'));
  chart.draw(data, options);
}
    </script>
        <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["corechart"]});
google.setOnLoadCallback(drawVisualization);

function drawVisualization() {
  // Some raw data (not necessarily accurate)
  var data = google.visualization.arrayToDataTable([
    ['Month', ''],
<c:forEach items="${losinglanelist.laneList}" var="lane" >
<c:set var="message" value="${lane.name}"/>
    ['<c:out value="${message}"/>',${lane.count}],    
</c:forEach>
    ['', 0]
  ]);

  var options = {
    title : 'Lanes most commonly used by losing players',
    vAxis: {title: "# of times  "},
    hAxis: {title: "Lanes "},
    seriesType: "bars",
    series: {5: {type: "line"}}
  };

  var chart = new google.visualization.ComboChart(document.getElementById('LanesL_div'));
  chart.draw(data, options);
}
    </script>
        <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["corechart"]});
google.setOnLoadCallback(drawVisualization);

function drawVisualization() {
  // Some raw data (not necessarily accurate)
  var data = google.visualization.arrayToDataTable([
    ['Month', ''],
<c:forEach items="${winningrolelist.roleList}" var="lane" >
<c:set var="message" value="${lane.name}"/>
    ['<c:out value="${message}"/>',${lane.count}],    
</c:forEach>
    ['', 0]
  ]);

  var options = {
    title : 'Role most commonly chosen in matches',
    vAxis: {title: "# of times role chosen by winning player"},
    hAxis: {title: "Role "},
    seriesType: "bars",
    series: {5: {type: "line"}}
  };

  var chart = new google.visualization.ComboChart(document.getElementById('RolesW_div'));
  chart.draw(data, options);
}
    </script>
            <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["corechart"]});
google.setOnLoadCallback(drawVisualization);

function drawVisualization() {
  // Some raw data (not necessarily accurate)
  var data = google.visualization.arrayToDataTable([
    ['Month', ''],
<c:forEach items="${losingrolelist.roleList}" var="lane" >
<c:set var="message" value="${lane.name}"/>
    ['<c:out value="${message}"/>',${lane.count}],    
</c:forEach>
    ['', 0]
  ]);

  var options = {
    title : 'Role most commonly chosen in matches',
    vAxis: {title: "# of times role chosen by losing player "},
    hAxis: {title: "Roles "},
    seriesType: "bars",
    series: {5: {type: "line"}}
  };

  var chart = new google.visualization.ComboChart(document.getElementById('RolesL_div'));
  chart.draw(data, options);
}
</script>
<style>
<style>
<style>
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
</head>
<body background="background_2.jpg" bgproperties="fixed">
<div id="dolphincontainer">
<div id="dolphinnav">
<form action="/PullData" method="get" >
<ul>
  <li><a href="/index.html" title=""><span>About Us</span></a></li>
  <li><a href="/ChampionSelect.jsp" title="" ><span>Champion Select</span></a></li>
  <li><a href="/DisplayData.jsp"><span>All Champs</span></a></li>
  <li><span><input type="text"  name="champ"/></span></li>
  <li><span><input type="submit" value="search"/></span></li>
 </ul>
</form>
</div>
</div>


<table class="bordered">
<tr>
	<td><img src="${champ.image}"></img>
	<font size="8" color="black">	${champ.name}</font></td>
</tr>
</table>
<table class="bordered">
<tr>
	<td><h4>Games Played</h4></td>
	<td><h4>Wins</h4></td>
	<td><h4>Loses</h4></td>
	<td><h4>Win Ratio</h4></td>
	<td><h4>Loss Ratio</h4></td>
</tr>
<tr>
	<td>${champ.numberOfGames}</td>
	<td>${champ.wins}</td>
	<td>${champ.loses}</td>
	<td>${champ.winRatio}</td>
	<td>${champ.lossRatio}</td>
</tr>
</table>
<table class="bordered">
<tr>
	<center><font size="10" color="white">Winning Match Stats</font></center>
</tr>
<tr>
	<td>Item Most used</td>
	<td>Name</td>
	<td>Description</td>
	<td>Number of times used</td>
</tr>
<tr>
	<td><img src="${champ.winningItem.image}"/></td>
	<td>${champ.winningItem.name}</td>
	<td>${champ.winningItem.description}</td>
	<td><%= request.getSession().getAttribute("itemcount") %></td>
</tr>
<tr>
	<td>Spell Most Used</td>
	<td>Name</td>
	<td>Description</td>
	<td>Number of Times Used</td>
</tr>
<tr>
	<td><img src="${champ.winningSpell.image}"/></td>
	<td>${champ.winningSpell.name}</td>
	<td>${champ.winningSpell.description}</td>
	<td><%= request.getSession().getAttribute("spellcount") %></td>
</tr>
</table>
<table class="bordered">
<tr></tr>
<tr>
	<td>#1 Game Role</td>
	<td>Total Number of times role was played</td>
</tr>
<tr>
	<td><%= request.getSession().getAttribute("rolename") %></td>
	<td><%= request.getSession().getAttribute("rolecount") %></td>
</tr>
</table>
<table class="bordered">
<tr></tr>
<tr>
	<td>1# Lane</td>
	<td>Total number of time lane was played</td>
</tr>
<tr>
	<td><%= request.getSession().getAttribute("lanename") %></td>
	<td><%= request.getSession().getAttribute("lanecount") %></td>
</tr>
</table>
<table class="bordered">
<tr></tr>
<tr>
	<td>Most common Level Reached</td>
	<td>Number of times Level was reached</td>
</tr>
<tr>
	<td><%= request.getSession().getAttribute("level") %></td>
	<td><%= request.getSession().getAttribute("levelcount") %></td>
</tr>
</table>








<table class="bordered">
<tr>
	<center><font size="10" color="white">Losing Match Stats</font></center>
</tr>
<tr>
	<td>Item Most used</td>
	<td>Name</td>
	<td>Description</td>
	<td>Number of times used</td>
</tr>
<tr>
	<td><img src="${champ.losingItem.image}"/></td>
	<td>${champ.losingItem.name}</td>
	<td>${champ.losingItem.description}</td>
	<td><%= request.getSession().getAttribute("itemcount2") %></td>
</tr>
<tr>
	<td>Spell Most Used</td>
	<td>Name</td>
	<td>Description</td>
	<td>Number of Times Used</td>
</tr>
<tr>
	<td><img src="${champ.losingSpell.image}"/></td>
	<td>${champ.losingSpell.name}</td>
	<td>${champ.losingSpell.description}</td>
	<td><%= request.getSession().getAttribute("spellcount2") %></td>
</tr>
</table>
<table class="bordered">
<tr></tr>
<tr>
	<td>#1 Game Role</td>
	<td>Total Number of times role was played</td>
</tr>
<tr>
	<td><%= request.getSession().getAttribute("rolename2") %></td>
	<td><%= request.getSession().getAttribute("rolecount2") %></td>
</tr>
</table>
<table class="bordered">
<tr></tr>
<tr>
	<td>1# Lane</td>
	<td>Total number of time lane was played</td>
</tr>
<tr>
	<td><%= request.getSession().getAttribute("lanename2") %></td>
	<td><%= request.getSession().getAttribute("lanecount2") %></td>
</tr>
</table>
<table class="bordered">
<tr></tr>
<tr>
	<td>Most common Level Reached</td>
	<td>Number of times Level was reached</td>
</tr>
<tr>
	<td><%= request.getSession().getAttribute("level2") %></td>
	<td><%= request.getSession().getAttribute("levelcount2") %></td>
</tr>
</table>
<center>
  <center><font size="10" color="white">Spells</font></center>
<table class="bordered">
<tr></tr>
<tr>
	<td>Top Spell Charts</td>
</tr>
<tr>
	<td><div id="SpellW_div" style="width: 500px; height: 500px;"></div></td>
	<td><div id="SpellL_div" style="width: 500px; height: 500px;"></div></td>
</tr>
</table>
</center>
  <center><font size="10" color="white">Items</font></center>
<center>
<table class="bordered">
<tr></tr>
<tr>
	<td>Top Items Charts</td>
</tr>
<tr>
	<td><div id="ItemsW_div" style="width: 500px; height: 500px;"></div></td>
	<td><div id="ItemsL_div" style="width: 500px; height: 500px;"></div></td>
</tr>
</table>
</center>
  <center><font size="10" color="white">Lanes</font></center>
<center>
<table class="bordered">
<tr></tr>
<tr>
	<td>Top Lane Charts</td>
</tr>
<tr>
	<td><div id="LanesW_div" style="width: 500px; height: 500px;"></div></td>
	<td><div id="LanesL_div" style="width: 500px; height: 500px;"></div></td>
</tr>
</table>
</center>
  <center><font size="10" color="white">Roles</font></center>
<center>
<table class="bordered">
<tr></tr>
<tr>
	<td>Top Roles Charts</td>
</tr>
<tr>
	<td><div id="RolesW_div" style="width: 500px; height: 500px;"></div></td>
	<td><div id="RolesL_div" style="width: 500px; height: 500px;"></div></td>
</tr>
</table>
</center>
</body>
</html>
