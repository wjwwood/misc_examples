// Code specific to the AUXOS Project AND the EM61MK2
// This might be abstractable
// This is the "wrapper" to get from the library to the platform
class EM61MK2Control {
public:
    EM61MK2Control() {
        this->configure = false;
    }
    
    EM61MK2Control(AUXOSServer *auxos_server, std::string port, int baudrate) {
        this->configure(auxos_server, port, baudrate);
    }
    
    void configure(AUXOSServer *auxos_server, std::string port = "COM1", int baudrate = 115200) {
        this->auxos_server = auxos_server;
        this->port = port;
        this->baudrate = this->baudrate;
        this->configured = true;
    }
    
    void start() {
        
    }
    
    void stop() {
        
    }
    
    void handleData(em61mk2_ns::EM61MK2Data &em_data) {
        
    }
    
private:
    AUXOSServer *auxos_server;
    em61mk2_ns::EM61MK2 
    bool configured;
};

// Glue code, gateway to comms, time, logging, configurations
// This is the platform (replaces MOOS, ROS, JAUS, etc...)
class AUXOSServer {
public:
    AUXOSServer() {}
    
    void getAUXOSConfigurations() {
        // Simulate getting configs from GUI or disk
        this->number_of_ems = 3;
        this->my_em61mk2_ports = {'COM1', 'COM2', 'COM3'};
        this->my_em61mk2_baudrates = {115200, 115200, 115200};
    }
    
    void configureEM61MK2s() {
        this->my_em61mk2_controls.resize(this->number_of_ems);
        for(size_t i = 0; i < this->number_of_ems; ++i) {
            this->my_em61mk2_controls[i] = 
                        em61mk2_ns::EM61MK2(this, 
                                         this->my_em61mk2_ports[i],
                                         this->my_em61mk2_baudrates[i]);
        }
    }
    
private:
    int number_of_ems;
    std::vector<EM61MK2Control> my_em61mk2_controls;
    // These could be in a vector of em61mk2config structs
    std::vector<std::string> my_em61mk2_ports;
    std::vector<int> my_em61mk2_baudrates;
    
};