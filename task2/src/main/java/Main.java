import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import static java.lang.Thread.sleep;

public class Main {
    public static void main(String[] args) throws IOException, InterruptedException {
        System.out.println("Python interpreter path: ");
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String path = reader.readLine();
        Thread elapsedTimeCountingThread = new Thread(() -> {
            int i = 0;
            while (true) {
                try {
                    sleep(1000);
                    System.out.println("Time elapsed: " + ++i + "s");
                } catch (InterruptedException e) {
                    break;
                }
            }
        });
        var processBuilder = new ProcessBuilder();
        processBuilder.command(path, "-m", "timeit", "-r 10");

        var process = processBuilder.start();

        elapsedTimeCountingThread.start();
        process.waitFor();
        elapsedTimeCountingThread.interrupt();
        elapsedTimeCountingThread.join();

        try (var processReader = new BufferedReader(new InputStreamReader(process.getInputStream()))) {
            String line;
            while ((line = processReader.readLine()) != null) {
                System.out.println(line);
            }
        }
    }
}
