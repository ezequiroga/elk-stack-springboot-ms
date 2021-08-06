package com.elk.logs.controllers;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 *
 * @author Eze Q.
 * @version
 * @since
 */
@RestController
public class GreetingController {

    private final Logger logger = LoggerFactory.getLogger(this.getClass());
    
    @GetMapping(value = "/")
    public ResponseEntity greeting(){
        logger.info("Greeting invoked");
        return ResponseEntity.ok("Hello!");
    }
    
}