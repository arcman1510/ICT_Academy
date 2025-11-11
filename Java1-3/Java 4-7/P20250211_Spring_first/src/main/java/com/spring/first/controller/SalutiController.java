package com.spring.first.controller;

import java.time.LocalTime;
import java.time.LocalDate;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(path="/saluto")
public class SalutiController {
	
	
	public SalutiController() {
		System.out.println("Spring istanzia SalutiController...");
	}
	
	@GetMapping(path="/generico")
	public String salutoGenerico() {
		return "Hello World!";
	}
	@GetMapping(path="/pers")
	public String salutoPers(String nome) {
		return "Hello " + nome;
	}
	@GetMapping(path="/data")
	public String localDate() {
		LocalDate date = LocalDate.now();
		LocalTime orario = LocalTime.now();	
		return date + " " + orario;
		
	}
}
