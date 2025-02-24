// SensorModule.java
package gb.hardware.arduinocarrier;

import gb.hardware.arduino.ArduinoMKR1010; // Importing ArduinoModule

import org.osgi.framework.BundleActivator;
import org.osgi.framework.BundleContext;

public class ArduinoIOTCarrier implements BundleActivator {
    public void start(BundleContext context) throws Exception {
        System.out.println("Sensor module started");
        // Assume some code here that uses functionality provided by ArduinoModule
    }

    public void stop(BundleContext context) throws Exception {
        System.out.println("Sensor module stopped");
    }
}
