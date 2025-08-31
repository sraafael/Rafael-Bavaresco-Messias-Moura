module br.com.curso.listatarefasdesktop {
    requires javafx.controls;
    requires javafx.fxml;


    opens br.com.curso.listatarefasdesktop to javafx.fxml;
    exports br.com.curso.listatarefasdesktop;
}