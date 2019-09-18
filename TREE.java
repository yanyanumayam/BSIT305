import javax.swing.JFrame;
import javax.swing.JTree;
import javax.swing.SwingUtilities;
import javax.swing.tree.DefaultMutableTreeNode;
public class TREE extends JFrame
{
private JTree tree;
public TREE()
{
//create the root node
DefaultMutableTreeNode root = new DefaultMutableTreeNode("html");
//create the child nodes
DefaultMutableTreeNode head = new DefaultMutableTreeNode("head");
DefaultMutableTreeNode title = new DefaultMutableTreeNode("title");
DefaultMutableTreeNode meta = new DefaultMutableTreeNode("meta");
DefaultMutableTreeNode body = new DefaultMutableTreeNode("body");
DefaultMutableTreeNode ul = new DefaultMutableTreeNode("ul");
DefaultMutableTreeNode li = new DefaultMutableTreeNode("li");
DefaultMutableTreeNode liNode = new DefaultMutableTreeNode("li");
DefaultMutableTreeNode h1 = new DefaultMutableTreeNode("h1");

//add the child nodes to the root node
DefaultMutableTreeNode h2 = new DefaultMutableTreeNode("h2");
DefaultMutableTreeNode a = new DefaultMutableTreeNode("a");


root.add(head);
root.add(body);

head.add(meta);
head.add(title);

body.add(ul);
body.add(h1);
body.add(h2);

ul.add(li);
ul.add(liNode);

h2.add(a);


//create the tree by passing in the root node
tree = new JTree(root);
add(tree);







this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
this.setTitle("JTree Example");
this.pack();
this.setVisible(true);
}

public static void main(String[] args)
{
SwingUtilities.invokeLater(new Runnable() {
@Override
public void run() {
new TREE();
}
});
}
}