module com.sadhu.fend {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.sadhu.fend to javafx.fxml;
    exports com.sadhu.fend;
}