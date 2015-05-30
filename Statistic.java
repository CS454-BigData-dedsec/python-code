package model;
 
import java.io.*;
import java.util.*;
import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.WebServlet;

@WebServlet("/Statistics")
public class Statistics extends HttpServlet {

  @Override
  public void doGet(HttpServletRequest request, HttpServletResponse response)
               throws IOException, ServletException {
    String victim ;
    String[] items = new String[7];
    String[] spells = new String[2];
    String lane;
    String role;
    int precent;

    /*
    response.setContentType("text/html;charset=UTF-8");
    PrintWriter out = response.getWriter();
    
    try {
      out.println("Hi how are you doing");  // HTML 5
    } finally {
      out.close();  // Always close the output writer
    }
    */
    //these abouve were the old files that i just wanted to keep for 
    //debugging since its been a while since I coded servlets

    // okay create the champ stats class and then have that collect all the info
    //ChampStatsBean champ = new ChampStatsBean();


    //stuff we will need is VictimsIDName , 
    //The CHampion , Items Selected ,  Spells , Lane Chosen, Role
    victim = request.getParameter("victim");
    items[0] = request.getParameter("item1");
    items[1] = request.getParameter("item2");
    items[2] = request.getParameter("item3");
    items[3] = request.getParameter("item4");
    items[4] = request.getParameter("item5");
    items[5] = request.getParameter("item6");
    items[6] = request.getParameter("item7");
    spells[0] = request.getParameter("spell1");
    spells[1] = request.getParameter("spell2");
    role = request.getParameter("role");
    lane = request.getParameter("lane");


    
    ChampionStats champ = new ChampionStats(victim,items,spells,role,lane);
    String beNice = champ.ChampionList();


    response.setContentType("text/html;charset=UTF-8");
    PrintWriter out = response.getWriter();
    out.println(g);     
    
  }
}
