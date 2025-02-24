package software.arducam.code;

import org.osgi.framework.BundleActivator;
import org.osgi.framework.BundleContext;

public class ArduCAMcode implements BundleActivator {
    public void start(BundleContext context) throws Exception {
        System.out.println("Software module started");
    }

    public void stop(BundleContext context) throws Exception {
        System.out.println("Software module stopped");
    }
}