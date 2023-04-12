package com.sadhu.fend;

import java.io.*;
import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.image.ImageView;

public class HelloController {
    public TextField ans;
    public ImageView captchaImg;
    public Label timeText;
    public TextField time_taken;
    @FXML
    private Label welcomeText;

    @FXML
    protected void onHelloButtonClick() throws IOException {
        ProcessBuilder builder = new ProcessBuilder("C:\\Users\\sadhu\\Documents\\captcharf\\Scripts\\python.exe", "..\\evaluator.py", ans.getText(), time_taken.getText());
        builder.redirectErrorStream(true);
        Process p = builder.start();
        BufferedReader r = new BufferedReader(new InputStreamReader(p.getInputStream()));
        String line;
        while (true) {
            line = r.readLine();
            if (line == null) { break; }
            System.out.println(line);
        }
        welcomeText.setText("New CAPTCHA generated! Reload to view.");
        timeText.setText("");
    }
}