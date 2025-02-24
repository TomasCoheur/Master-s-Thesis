package hardware.niclavision;

import org.osgi.framework.BundleActivator;
import org.osgi.framework.BundleContext;

public class NiclaVision implements BundleActivator {
    public void start(BundleContext context) throws Exception {
        System.out.println("Hardware module started");
    }

    public void stop(BundleContext context) throws Exception {
        System.out.println("Hardware module stopped");
    }
}